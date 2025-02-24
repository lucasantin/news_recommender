import subprocess
import json
import os

class NewsRecommender:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def recommend(self, user_id, k=10):
        try:
            result = subprocess.run(
                ['python', 'topk.py', str(user_id), str(k)],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.base_dir
            )
            # Debugging outputs
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")

            # Attempt to parse JSON from stdout
            recommendations = json.loads(result.stdout.strip())
            print(f"Parsed keys: {list(recommendations.keys())}")

            # Ensure key matching by stripping spaces
            cleaned_user_id = user_id.strip()
            return recommendations.get(cleaned_user_id, [])
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar topk.py: {e}")
            print(f"Saída de erro: {e.stderr}")
            return []
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print(f"Saída do script: {result.stdout}")
            return []
