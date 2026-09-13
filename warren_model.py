"""
warren_model.py
CSC505 - Critical Thinking Assignment: The Warren Adaptive Model

Prompts the user for each phase name and a short description, then
outputs a well-formatted summary of the model's phases and structure.

The Warren Adaptive Model modernizes the traditional Waterfall Model
(Pressman & Maxim, 2020) by wrapping its sequential phases in iterative
feedback loops drawn from Agile, Spiral, and DevOps practices.

Author: C. Warren
"""


def get_positive_int(prompt: str, default: int) -> int:
    """Ask the user for a positive integer, falling back to a default."""
    raw = input(f"{prompt} [default {default}]: ").strip()
    if not raw:
        return default
    try:
        value = int(raw)
        if value > 0:
            return value
        print(f"  Value must be positive; using default of {default}.")
    except ValueError:
        print(f"  '{raw}' is not a number; using default of {default}.")
    return default


def collect_phases(count: int) -> list[dict]:
    """Prompt the user for each phase's name and short description."""
    phases = []
    for i in range(1, count + 1):
        print(f"\n--- Phase {i} of {count} ---")
        name = input("  Phase name: ").strip() or f"Phase {i}"
        description = input("  Short description: ").strip() or "(no description provided)"
        phases.append({"number": i, "name": name, "description": description})
    return phases


def print_summary(model_name: str, phases: list[dict]) -> None:
    """Print a formatted summary of the model's phases and structure."""
    width = 68
    print()
    print("=" * width)
    print(f"{model_name:^{width}}")
    print("=" * width)

    for phase in phases:
        print(f"Phase {phase['number']}: {phase['name']} - {phase['description']}")

    print("-" * width)
    print("Structure: Each phase ends with a feedback checkpoint. If the")
    print("checkpoint fails, work loops back to the phase indicated below")
    print("rather than proceeding, keeping the model adaptive to change.")
    print("-" * width)

    # Show the adaptive flow: forward arrows plus feedback loops.
    for i, phase in enumerate(phases):
        if i < len(phases) - 1:
            print(f"  {phase['name']}  -->  {phases[i + 1]['name']}")
    if len(phases) > 1:
        print(f"  {phases[-1]['name']}  ..>  {phases[0]['name']}   (continuous feedback loop)")
    print("=" * width)


def main() -> None:
    print("*" * 68)
    print("       The Warren Adaptive Model - Process Model Builder")
    print("*" * 68)
    print("Define the phases of your adaptive software process model.")

    count = get_positive_int("\nHow many phases does your model have?", default=5)
    phases = collect_phases(count)
    print_summary("The Warren Adaptive Model", phases)
    print("\nModel summary complete. Iterate early, iterate often!")


if __name__ == "__main__":
    main()
