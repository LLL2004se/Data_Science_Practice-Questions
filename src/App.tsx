import React, { useState } from 'react';
import { Shield, FileText, CheckCircle, XCircle, AlertCircle, Send } from 'lucide-react';

interface ClaimRequest {
  age: number;
  gender: string;
  procedure: string;
  location: string;
  policy_duration: string;
}

interface ClaimResponse {
  Decision: string;
  Amount: string;
  Justification: string;
  Clauses_Referenced: string[];
}

function App() {
  const [formData, setFormData] = useState<ClaimRequest>({
    age: 0,
    gender: '',
    procedure: '',
    location: '',
    policy_duration: ''
  });
  
  const [response, setResponse] = useState<ClaimResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'age' ? parseInt(value) || 0 : value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    // Simulate API call with mock response
    setTimeout(() => {
      const mockResponse: ClaimResponse = {
        Decision: formData.procedure.toLowerCase().includes('knee') && 
                 formData.policy_duration.includes('3 months') ? "Rejected" : "Approved",
        Amount: formData.procedure.toLowerCase().includes('knee') && 
               formData.policy_duration.includes('3 months') ? "N/A" : "Up to Sum Insured",
        Justification: formData.procedure.toLowerCase().includes('knee') && 
                      formData.policy_duration.includes('3 months') 
                      ? "The policyholder's request for knee surgery is rejected because 'Joint replacement surgery' is listed under the 'Specified disease/procedure waiting period' (Code - Excl02), which requires a 24-month continuous coverage period before expenses related to it are covered. The current policy has only been active for 3 months, which does not meet this waiting period."
                      : "The claim meets all policy requirements and is approved for coverage.",
        Clauses_Referenced: [
          "Excl02 - Specified disease/procedure waiting period (24 months)",
          "Excl02 - Point 27: Joint replacement surgery",
          "General Coverage - Hospitalization benefits"
        ]
      };
      setResponse(mockResponse);
      setLoading(false);
    }, 2000);
  };

  const getDecisionIcon = (decision: string) => {
    switch (decision.toLowerCase()) {
      case 'approved':
        return <CheckCircle className="w-6 h-6 text-green-500" />;
      case 'rejected':
        return <XCircle className="w-6 h-6 text-red-500" />;
      default:
        return <AlertCircle className="w-6 h-6 text-yellow-500" />;
    }
  };

  const getDecisionColor = (decision: string) => {
    switch (decision.toLowerCase()) {
      case 'approved':
        return 'border-green-200 bg-green-50';
      case 'rejected':
        return 'border-red-200 bg-red-50';
      default:
        return 'border-yellow-200 bg-yellow-50';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center mb-4">
            <Shield className="w-12 h-12 text-indigo-600 mr-3" />
            <h1 className="text-4xl font-bold text-gray-800">PolicyProbe</h1>
          </div>
          <p className="text-xl text-gray-600">AI-Powered Insurance Claim Processing</p>
          <div className="mt-2 text-sm text-gray-500">
            Webhook URL: <code className="bg-gray-200 px-2 py-1 rounded">https://your-domain.com/api/webhook/claims</code>
          </div>
        </div>

        <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Claim Form */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <div className="flex items-center mb-6">
              <FileText className="w-6 h-6 text-indigo-600 mr-2" />
              <h2 className="text-2xl font-semibold text-gray-800">Submit Claim</h2>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Age
                  </label>
                  <input
                    type="number"
                    name="age"
                    value={formData.age || ''}
                    onChange={handleInputChange}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    placeholder="Enter age"
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Gender
                  </label>
                  <select
                    name="gender"
                    value={formData.gender}
                    onChange={handleInputChange}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    required
                  >
                    <option value="">Select gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Procedure/Treatment
                </label>
                <input
                  type="text"
                  name="procedure"
                  value={formData.procedure}
                  onChange={handleInputChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  placeholder="e.g., knee surgery, dental treatment"
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Location
                </label>
                <input
                  type="text"
                  name="location"
                  value={formData.location}
                  onChange={handleInputChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  placeholder="e.g., Mumbai, Delhi, Pune"
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Policy Duration
                </label>
                <input
                  type="text"
                  name="policy_duration"
                  value={formData.policy_duration}
                  onChange={handleInputChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  placeholder="e.g., 3 months, 2 years"
                  required
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-indigo-600 text-white py-3 px-4 rounded-lg hover:bg-indigo-700 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition-colors duration-200 flex items-center justify-center disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                ) : (
                  <>
                    <Send className="w-5 h-5 mr-2" />
                    Process Claim
                  </>
                )}
              </button>
            </form>
          </div>

          {/* Results Panel */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-6">Claim Decision</h2>
            
            {!response && !loading && (
              <div className="text-center py-12">
                <Shield className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                <p className="text-gray-500">Submit a claim to see the decision</p>
              </div>
            )}

            {loading && (
              <div className="text-center py-12">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto mb-4"></div>
                <p className="text-gray-600">Processing your claim...</p>
              </div>
            )}

            {response && (
              <div className={`border-2 rounded-lg p-6 ${getDecisionColor(response.Decision)}`}>
                <div className="flex items-center mb-4">
                  {getDecisionIcon(response.Decision)}
                  <h3 className="text-xl font-semibold ml-2">
                    Decision: {response.Decision}
                  </h3>
                </div>

                <div className="space-y-4">
                  <div>
                    <h4 className="font-medium text-gray-700">Coverage Amount:</h4>
                    <p className="text-lg font-semibold text-gray-900">{response.Amount}</p>
                  </div>

                  <div>
                    <h4 className="font-medium text-gray-700">Justification:</h4>
                    <p className="text-gray-800 leading-relaxed">{response.Justification}</p>
                  </div>

                  <div>
                    <h4 className="font-medium text-gray-700">Referenced Clauses:</h4>
                    <ul className="mt-2 space-y-1">
                      {response.Clauses_Referenced.map((clause, index) => (
                        <li key={index} className="text-sm text-gray-600 bg-white bg-opacity-50 px-3 py-1 rounded">
                          {clause}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Features Section */}
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
          <div className="bg-white rounded-lg p-6 text-center shadow-md">
            <CheckCircle className="w-12 h-12 text-green-500 mx-auto mb-3" />
            <h3 className="text-lg font-semibold mb-2">AI-Powered Analysis</h3>
            <p className="text-gray-600">Advanced algorithms analyze claims against policy terms</p>
          </div>
          
          <div className="bg-white rounded-lg p-6 text-center shadow-md">
            <FileText className="w-12 h-12 text-blue-500 mx-auto mb-3" />
            <h3 className="text-lg font-semibold mb-2">Instant Processing</h3>
            <p className="text-gray-600">Get claim decisions in seconds, not days</p>
          </div>
          
          <div className="bg-white rounded-lg p-6 text-center shadow-md">
            <Shield className="w-12 h-12 text-indigo-500 mx-auto mb-3" />
            <h3 className="text-lg font-semibold mb-2">Accurate Decisions</h3>
            <p className="text-gray-600">Precise evaluation based on policy clauses</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;