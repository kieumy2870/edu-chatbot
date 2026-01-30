"""Test script for the AI Math Tutor system.

This script tests the math solving functionality without running the full API.
"""
from ai_service import solve_math_problem


def test_text_problem():
    """Test solving a math problem from text."""
    print("=" * 60)
    print("TEST 1: Solving from text input")
    print("=" * 60)
    
    problem = "Giải phương trình bậc hai: x^2 - 5x + 6 = 0"
    print(f"\n📝 Problem: {problem}\n")
    
    solution = solve_math_problem(problem)
    print(f"✅ Solution:\n{solution}\n")


def test_calculus_problem():
    """Test a calculus problem."""
    print("=" * 60)
    print("TEST 2: Calculus problem")
    print("=" * 60)
    
    problem = "Tính đạo hàm của hàm số f(x) = x^3 + 2x^2 - 5x + 1"
    print(f"\n📝 Problem: {problem}\n")
    
    solution = solve_math_problem(problem)
    print(f"✅ Solution:\n{solution}\n")


def test_geometry_problem():
    """Test a geometry problem."""
    print("=" * 60)
    print("TEST 3: Geometry problem")
    print("=" * 60)
    
    problem = """
    Cho tam giác ABC có:
    - Cạnh AB = 5 cm
    - Cạnh BC = 12 cm
    - Góc B = 90 độ
    Tính độ dài cạnh AC và diện tích tam giác ABC.
    """
    print(f"\n📝 Problem: {problem}\n")
    
    solution = solve_math_problem(problem)
    print(f"✅ Solution:\n{solution}\n")


def test_cache():
    """Test that caching works by solving the same problem twice."""
    print("=" * 60)
    print("TEST 4: Testing cache functionality")
    print("=" * 60)
    
    problem = "Tính 15 + 27"
    
    print(f"\n📝 Problem: {problem}")
    print("\n🔄 First call (should hit API)...")
    solution1 = solve_math_problem(problem)
    print(f"✅ Solution: {solution1[:100]}...\n")
    
    print("🔄 Second call (should use cache)...")
    solution2 = solve_math_problem(problem)
    print(f"✅ Solution: {solution2[:100]}...\n")
    
    if "[KẾT QUẢ TỪ CACHE]" in solution2:
        print("✅ Cache is working correctly!\n")
    else:
        print("⚠️ Cache might not be working as expected.\n")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("   🤖 AI MATH TUTOR - SYSTEM TEST")
    print("=" * 60 + "\n")
    
    try:
        test_text_problem()
        test_calculus_problem()
        test_geometry_problem()
        test_cache()
        
        print("=" * 60)
        print("✅ ALL TESTS COMPLETED!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nMake sure:")
        print("1. Your .env file contains a valid GEMINI_API_KEY")
        print("2. You have internet connection")
        print("3. All dependencies are installed (pip install -r requirements.txt)")
