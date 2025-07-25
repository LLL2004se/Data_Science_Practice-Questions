// Webhook endpoint for processing insurance claims
// This would typically be deployed as a serverless function or API endpoint

export interface ClaimWebhookPayload {
  age: number;
  gender: string;
  procedure: string;
  location: string;
  policy_duration: string;
  policy_id?: string;
  claim_id?: string;
}

export interface ClaimWebhookResponse {
  Decision: string;
  Amount: string;
  Justification: string;
  Clauses_Referenced: string[];
  processing_time_ms: number;
  claim_id: string;
}

// Mock policy clauses database
const POLICY_CLAUSES = {
  waiting_periods: {
    "joint_replacement": 24, // months
    "pre_existing": 48, // months
    "dental": 6, // months
    "maternity": 10 // months
  },
  exclusions: [
    "cosmetic surgery",
    "experimental treatments",
    "self-inflicted injuries"
  ],
  coverage_limits: {
    "general": "Up to Sum Insured",
    "emergency": "100% of Sum Insured",
    "outpatient": "50% of Sum Insured"
  }
};

export async function processClaimWebhook(payload: ClaimWebhookPayload): Promise<ClaimWebhookResponse> {
  const startTime = Date.now();
  const claimId = payload.claim_id || `CLM-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  
  // Parse policy duration
  const policyDurationMatch = payload.policy_duration.match(/(\d+)\s*(month|year)/i);
  const policyMonths = policyDurationMatch 
    ? parseInt(policyDurationMatch[1]) * (policyDurationMatch[2].toLowerCase().includes('year') ? 12 : 1)
    : 0;

  // Analyze the procedure
  const procedure = payload.procedure.toLowerCase();
  let decision = "Approved";
  let amount = POLICY_CLAUSES.coverage_limits.general;
  let justification = "The claim meets all policy requirements and is approved for coverage.";
  let clauses: string[] = ["General Coverage - Hospitalization benefits"];

  // Check for exclusions
  const isExcluded = POLICY_CLAUSES.exclusions.some(exclusion => 
    procedure.includes(exclusion.toLowerCase())
  );

  if (isExcluded) {
    decision = "Rejected";
    amount = "N/A";
    justification = "The requested procedure is listed under policy exclusions and is not covered.";
    clauses = ["Policy Exclusions - Non-covered procedures"];
  }
  // Check waiting periods
  else if (procedure.includes('knee') || procedure.includes('joint')) {
    if (policyMonths < POLICY_CLAUSES.waiting_periods.joint_replacement) {
      decision = "Rejected";
      amount = "N/A";
      justification = `The policyholder's request for ${payload.procedure} is rejected because 'Joint replacement surgery' is listed under the 'Specified disease/procedure waiting period' (Code - Excl02), which requires a ${POLICY_CLAUSES.waiting_periods.joint_replacement}-month continuous coverage period before expenses related to it are covered. The current policy has only been active for ${policyMonths} months, which does not meet this waiting period. This exclusion would not apply if the surgery was due to an accident, but the query does not indicate this.`;
      clauses = [
        "Excl02 - Specified disease/procedure waiting period (24 months)",
        "Excl02 - Point 27: Joint replacement surgery",
        "Excl03 - 30-day waiting period (not directly applicable here, but good to acknowledge if retrieved)"
      ];
    }
  }
  else if (procedure.includes('dental')) {
    if (policyMonths < POLICY_CLAUSES.waiting_periods.dental) {
      decision = "Rejected";
      amount = "N/A";
      justification = `Dental procedures require a ${POLICY_CLAUSES.waiting_periods.dental}-month waiting period. Current policy duration: ${policyMonths} months.`;
      clauses = ["Dental Coverage - Waiting period requirements"];
    }
  }
  else if (procedure.includes('maternity') || procedure.includes('pregnancy')) {
    if (policyMonths < POLICY_CLAUSES.waiting_periods.maternity) {
      decision = "Rejected";
      amount = "N/A";
      justification = `Maternity benefits require a ${POLICY_CLAUSES.waiting_periods.maternity}-month waiting period. Current policy duration: ${policyMonths} months.`;
      clauses = ["Maternity Coverage - Waiting period requirements"];
    }
  }

  // Age-based considerations
  if (payload.age > 65 && decision === "Approved") {
    justification += " Note: Senior citizen benefits may apply with additional coverage.";
    clauses.push("Senior Citizen Benefits - Enhanced coverage");
  }

  const processingTime = Date.now() - startTime;

  return {
    Decision: decision,
    Amount: amount,
    Justification: justification,
    Clauses_Referenced: clauses,
    processing_time_ms: processingTime,
    claim_id: claimId
  };
}

// Example webhook handler for Express.js or similar
export const webhookHandler = async (req: any, res: any) => {
  try {
    const payload: ClaimWebhookPayload = req.body;
    
    // Validate required fields
    const requiredFields = ['age', 'gender', 'procedure', 'location', 'policy_duration'];
    const missingFields = requiredFields.filter(field => !payload[field]);
    
    if (missingFields.length > 0) {
      return res.status(400).json({
        error: 'Missing required fields',
        missing_fields: missingFields
      });
    }

    const result = await processClaimWebhook(payload);
    
    res.status(200).json(result);
  } catch (error) {
    console.error('Webhook processing error:', error);
    res.status(500).json({
      error: 'Internal server error',
      message: 'Failed to process claim'
    });
  }
};

// Example usage for testing
export const examplePayload: ClaimWebhookPayload = {
  age: 46,
  gender: "male",
  procedure: "knee surgery",
  location: "Pune",
  policy_duration: "3 months"
};