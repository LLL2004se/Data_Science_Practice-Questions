# PolicyProbe - AI-Powered Insurance Claim Processing

A hackathon project that demonstrates intelligent insurance claim processing using AI and policy analysis.

## 🚀 Features

- **AI-Powered Analysis**: Advanced algorithms analyze claims against policy terms
- **Instant Processing**: Get claim decisions in seconds, not days
- **Accurate Decisions**: Precise evaluation based on policy clauses
- **Webhook Integration**: RESTful API for external system integration
- **Real-time UI**: Interactive web interface for claim submission

## 🛠️ Technology Stack

- **Frontend**: React + TypeScript + Tailwind CSS
- **Icons**: Lucide React
- **Build Tool**: Vite
- **Deployment**: Ready for Netlify/Vercel

## 📋 API Endpoints

### Webhook URL
```
POST https://your-domain.com/api/webhook/claims
```

### Request Payload
```json
{
  "age": 46,
  "gender": "male",
  "procedure": "knee surgery",
  "location": "Pune",
  "policy_duration": "3 months",
  "policy_id": "optional",
  "claim_id": "optional"
}
```

### Response Format
```json
{
  "Decision": "Rejected",
  "Amount": "N/A",
  "Justification": "The policyholder's request for knee surgery is rejected because...",
  "Clauses_Referenced": [
    "Excl02 - Specified disease/procedure waiting period (24 months)",
    "Excl02 - Point 27: Joint replacement surgery"
  ],
  "processing_time_ms": 150,
  "claim_id": "CLM-1234567890-abc123"
}
```

## 🏥 Policy Rules Implemented

### Waiting Periods
- **Joint Replacement Surgery**: 24 months
- **Pre-existing Conditions**: 48 months  
- **Dental Procedures**: 6 months
- **Maternity Benefits**: 10 months

### Exclusions
- Cosmetic surgery
- Experimental treatments
- Self-inflicted injuries

### Coverage Limits
- **General**: Up to Sum Insured
- **Emergency**: 100% of Sum Insured
- **Outpatient**: 50% of Sum Insured

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm run dev
   ```

3. **Build for Production**
   ```bash
   npm run build
   ```

## 🔗 Webhook Integration

To integrate with external systems, send POST requests to the webhook endpoint with the required payload format. The system will:

1. Validate the input data
2. Apply policy rules and waiting periods
3. Check for exclusions
4. Generate a decision with justification
5. Return structured response with referenced clauses

## 🎯 Use Cases

- **Insurance Companies**: Automate claim processing
- **Healthcare Providers**: Real-time eligibility verification
- **Third-party Administrators**: Streamline claim workflows
- **Mobile Apps**: Instant claim status updates

## 🔧 Customization

The policy rules are easily configurable in `src/api/webhook.ts`. Modify the `POLICY_CLAUSES` object to adjust:

- Waiting periods for different procedures
- Coverage exclusions
- Amount limits
- Age-based benefits

## 📊 Example Scenarios

### Approved Claim
- **Input**: 35-year-old requesting dental cleaning, policy active for 8 months
- **Output**: Approved with full coverage

### Rejected Claim  
- **Input**: 46-year-old requesting knee surgery, policy active for 3 months
- **Output**: Rejected due to 24-month waiting period

### Conditional Approval
- **Input**: 70-year-old requesting general surgery, policy active for 2 years
- **Output**: Approved with senior citizen benefits

## 🏆 Hackathon Highlights

- **Problem Solved**: Manual claim processing delays
- **Innovation**: AI-driven policy interpretation
- **Impact**: Reduced processing time from days to seconds
- **Scalability**: Webhook architecture supports high volume
- **User Experience**: Intuitive interface with real-time feedback

## 📝 License

This project was created for hackathon purposes and is available for educational use.

---

**Built with ❤️ for the hackathon**