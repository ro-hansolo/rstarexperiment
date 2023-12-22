from r_star_search import RStarSearch
import asyncio

def main():
    query = "Machine A puts out a yo-yo every 6 minutes. Machine B puts out a yo-yo every 9 minutes. After how many minutes will they have produced 10 yo-yos?"
    r_star = RStarSearch(user_query=query, generator_model_path="iinsert path to gguf model", n_samples=10, max_tokens_per_turn=100,API_KEY="insert openai key here")
    asyncio.run(r_star.run_search())

if __name__ == "__main__":
    main()
# {"question": "Machine A puts out a yo-yo every 6 minutes. Machine B puts out a yo-yo every 9 minutes. After how many minutes will they have produced 10 yo-yos?", "options": ["A)24 minutes", "B)32 minutes", "C)36 minutes", "D)64 minutes", "E)72 minutes"]