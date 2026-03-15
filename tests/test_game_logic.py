from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

# TEST CASES: Created by Agent
def test_hints_not_inverted_too_high():
    # Bug: guess > secret was returning "Too Low" instead of "Too High"
    outcome, _ = check_guess(75, 50)
    assert outcome == "Too High", (
        f"Expected 'Too High' when guess (75) > secret (50), got '{outcome}'. "
        "Hints may still be inverted."
    )

def test_hints_not_inverted_too_low():
    # Bug: guess < secret was returning "Too High" instead of "Too Low"
    outcome, _ = check_guess(25, 50)
    assert outcome == "Too Low", (
        f"Expected 'Too Low' when guess (25) < secret (50), got '{outcome}'. "
        "Hints may still be inverted."
    )

def test_hints_not_inverted_boundary_high():
    # One above the secret — should still be Too High, not Too Low
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_hints_not_inverted_boundary_low():
    # One below the secret — should still be Too Low, not Too High
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"
