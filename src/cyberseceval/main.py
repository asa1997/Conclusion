from cyberseceval.crew import crew

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
    result = crew.kickoff(inputs=report_paths)
    with open("llm_security_conclusion.md", "w") as f:
        f.write(result)
    print("✅ Report saved to llm_security_conclusion.md")
