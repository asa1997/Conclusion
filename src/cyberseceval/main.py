import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cyberseceval.crew import ConclusionCrew

report_paths = {
  "mitre_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-mitre-test-detailed-report.json",
  "frr_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-frr-test-detailed-report.json",
  "instruct_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-instruct-test-detailed-report.json",
  "autocomplete_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-autocomplete-test-detailed-report.json",
  "prompt_injection_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-prompt-injection-test-detailed-report.json",
  "interpreter_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-interpreter-test-detailed-report.json",
  "phishing_file": "/home/ubuntu/besecure-ml-assessment-datastore/models/DeepSeek-R1:7b/llm-benchmark/DeepSeek-R1:7b-spear-phishing-test-detailed-report.json"
}

if __name__ == "__main__":
    # result = crew.kickoff(inputs=report_paths)
    try:
      crew_instance = ConclusionCrew().crew()  # ⬅ instantiate and call `crew()`
      result = crew_instance.kickoff(inputs=report_paths)
      with open("llm_security_conclusion.md", "w") as f:
          f.write(result)
      print("✅ Report saved to llm_security_conclusion.md")
    except Exception as e:
      import traceback
      print("❌ An error occurred while generating the report:")
      traceback.print_exc()
