import random
import time
import sys

def display_banner():
    """Display a stylish lottery banner"""
    print("\n" + "═" * 50)
    print("║" + " " * 14 + "🎰 LUCKY LOTTERY 🎰" + " " * 14 + "║")
    print("║" + " " * 12 + "4-Digit Number Generator" + " " * 12 + "║")
    print("═" * 50)

def animate_rolling(duration=1.5):
    """Create a rolling animation effect"""
    print("\n🎲 Rolling the numbers", end="")
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in [".", "..", "...", "   "]:
            print(f"\r🎲 Rolling the numbers{symbol}", end="")
            sys.stdout.flush()
            time.sleep(0.15)
    print()

def generate_lottery_number():
    """Generate a random 4-digit lottery number"""
    return random.randint(0, 9999)

def display_result(number):
    """Display the lottery number in a fancy format"""
    # Format number with leading zeros
    formatted = f"{number:04d}"
    
    print("\n" + "┌" + "─" * 7 + "┬" + "─" * 7 + "┬" + "─" * 7 + "┬" + "─" * 7 + "┐")
    print(f"│   {formatted[0]}   │   {formatted[1]}   │   {formatted[2]}   │   {formatted[3]}   │")
    print("└" + "─" * 7 + "┴" + "─" * 7 + "┴" + "─" * 7 + "┴" + "─" * 7 + "┘")
    print(f"\n🎉 Your Lucky Number: {formatted}")

def display_statistics(history):
    """Display statistics of generated numbers"""
    if not history:
        print("\nNo numbers generated yet!")
        return
    
    print("\n📊 Statistics:")
    print(f"   Numbers generated: {len(history)}")
    print(f"   Highest: {max(history):04d}")
    print(f"   Lowest: {min(history):04d}")
    print(f"   Recent numbers: {', '.join(f'{n:04d}' for n in history[-5:])}")

def main():
    """Main lottery application"""
    history = []
    
    display_banner()
    
    while True:
        print("\n" + "─" * 50)
        print("Options:")
        print("  [1] 🎰 Generate Lucky Number")
        print("  [2] 🎰 Generate Multiple Numbers")
        print("  [3] 📊 View Statistics")
        print("  [4] 🚪 Exit")
        print("─" * 50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            animate_rolling()
            number = generate_lottery_number()
            history.append(number)
            display_result(number)
            
        elif choice == "2":
            try:
                count = int(input("How many numbers to generate? (1-10): "))
                count = max(1, min(10, count))  # Clamp between 1 and 10
                
                print(f"\n🎰 Generating {count} lucky numbers...")
                animate_rolling(0.8)
                
                print("\n" + "═" * 40)
                for i in range(count):
                    number = generate_lottery_number()
                    history.append(number)
                    print(f"  #{i+1}: 【 {number:04d} 】")
                print("═" * 40)
                
            except ValueError:
                print("⚠️  Please enter a valid number!")
                
        elif choice == "3":
            display_statistics(history)
            
        elif choice == "4":
            print("\n🍀 Good luck with your numbers! Goodbye! 🍀\n")
            break
            
        else:
            print("⚠️  Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
