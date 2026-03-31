def main():
    MAX_OPTIONS = 10
    MAX_FACTORS = 10

    print("\n" + "🚀" * 50)
    print("      Hey! Welcome to DECISION BUDDY 🤝")
    print("    Making tough choices stupidly easy!")
    print("🚀" * 50 + "\n")

    print("👋 Quick start: We're gonna weigh your options like pros!")
    print("   Enter stuff, rate importance, I'll do the math magic ✨\n")

    # Options - the big choices
    print("🎯 FIRST: Your options (like 'Netflix' vs 'Gym' vs 'Sleep')")
    while True:
        try:
            option_count = int(input("How many options you got? (2-10): "))
            if 2 <= option_count <= MAX_OPTIONS:
                break
            print("😂 C'mon, 2 to 10 only! Try again.")
        except:
            print("Numbers buddy! Just a number! 😅")

    options = []
    print(f"\nSweet! Spill the {option_count} options:")
    for i in range(option_count):
        while True:
            option = input(f"  {i+1}. ").strip()
            if option:
                options.append(option)
                break
            print("Tell me something! Can't be blank! 😉")

    # Factors - what makes options good/bad
    print(f"\n📊 NEXT: What matters most? (price, fun, health, etc)")
    while True:
        try:
            factor_count = int(input("How many factors? (1-10): "))
            if 1 <= factor_count <= MAX_FACTORS:
                break
            print("1-10 max! Don't make me count to 11! 😜")
        except:
            print("Numberrrrssss! 😤")

    factors = []
    print("Name 'em! (be specific - helps later)")
    for i in range(factor_count):
        factor = input(f"  Factor {i+1}: ").strip()
        factors.append(factor)

    # Weights - how much each factor matters to YOU
    print(f"\n⚖️  IMPORTANCE TIME! Rate 0-10 (10 = 'make or break')")
    weights = []
    for factor in factors:
        print(f"\n💡 How crucial is '{factor}'?")
        while True:
            try:
                inp = input("Your weight (0-10): ")
                weight = float(inp)
                if 0 <= weight <= 10:
                    weights.append(weight)
                    print(f"   Got it! {factor} = {weight}/10")
                    break
                print("0-10 only! No 11s or negatives! 🙄")
            except:
                print("Gimme a real number! 🧮")

    # THE FUN PART - scoring!
    print(f"\n{'='*60}")
    print("🎮 SCORING TIME! Rate each option 0-10 per factor")
    print("   (0 = trash, 10 = perfection) 🚀")
    print('='*60 + "\n")

    scores = []
    for idx, option in enumerate(options):
        print(f"\n{'🔥':>3} JUDGING: {option.upper()} 🔥")
        print("-" * 40)
        
        current_score = 0.0
        for factor in factors:
            print(f"   {factor.ljust(20)}?", end=" ")
            while True:
                try:
                    score = float(input("Score: "))
                    if 0 <= score <= 10:
                        weighted = score * weights[factors.index(factor)]
                        current_score += weighted
                        print(f"   ✓ {score}/10 (adds {weighted:.1f})")
                        break
                    print("  0-10! Be real! 😏")
                except:
                    print("  Number! 0-10! Let's go! 💥")
        
        scores.append(current_score)
        print(f"\n   🧮 TOTAL for {option}: {current_score:.2f}")
        print("-" * 40)

    # Drumroll... winner!
    best_score = max(scores)
    best_index = scores.index(best_score)
    
    print("\n" + "🎊" * 60)
    print("                FINAL SHOWDOWN! 🥇")
    print("🎊" * 60)
    print()
    
    # Results table
    print("RANKING:".center(50))
    print(" " + "-"*50)
    for i in range(len(options)):
        bar = "█" * int(scores[i]/max(scores)*20) if scores[i] > 0 else ""
        print(f"{i+1}. {options[i]:<25} {scores[i]:>7.2f} {bar}")
    print(" " + "-"*50)
    
    print(f"\n🏆 WINNER WINNER! '{options[best_index]}' scores {best_score:.2f}!")
    print(f"   That's {best_score/max(scores)*100:.1f}% better than average! 🎉")
    
    print("\n💭 Pro tip: Second-guess if it feels right. Math helps, gut rules! 😉")
    print("\nRun again? Tweak scores? Your call! 👋")

if __name__ == "__main__":
    main()