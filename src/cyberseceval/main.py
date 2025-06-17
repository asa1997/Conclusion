from src.cyberseceval.crew import crew

report_paths = {
  "mitre_file": "data/mitre.json",
  "frr_file": "data/frr.json",
  "instruct_file": "data/instruct.json",
  "autocomplete_file": "data/autocomplete.json",
  "prompt_injection_file": "data/prompt_injection.json",
  "interpreter_file": "data/code_interp.json",
  "phishing_file": "data/phishing.json"
}

if __name__ == "__main__":
    result = crew.kickoff(inputs=report_paths)
    with open("llm_security_conclusion.md", "w") as f:
        f.write(result)
    print("✅ Report saved to llm_security_conclusion.md")
