import random
from pathlib import Path

def random_game(score_file_path: str = "High_score.txt") -> int:
    print("Welcome to the Random Game!")
    score = random.randint(1, 100)
    
    file_path = Path(score_file_path)
    
    # Ensure file exists to prevent FileNotFoundError
    if not file_path.exists():
        file_path.write_text("0")
        
    try:
        content = file_path.read_text().strip()
        hi_score = int(content) if content else 0
    except ValueError:
        hi_score = 0

    if score > hi_score:
        print(f"🔥 New high score set: {score} (Previous: {hi_score})")
        file_path.write_text(str(score))
    else:
        print(f"Your score: {score} | Current High Score: {hi_score}")
        
    return score

if __name__ == "__main__":
    random_game()