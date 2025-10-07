import random
import itertools

PIECES_FOR_COMBOS = ["bishop", "knight", "rook", "queen", "king"]

class ChessPlayer:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age if age is not None else random.randint(12, 50)
        self.growth_potential = random.randint(0, 100)

        # --- Basic piece strengths
        self.pawn_strength   = random.randint(0, 100)
        self.bishop_strength = random.randint(0, 100)
        self.knight_strength = random.randint(0, 100)
        self.rook_strength   = random.randint(0, 100)
        self.queen_strength  = random.randint(0, 100)
        self.king_safety_awareness = random.randint(0, 100)

        # --- Combo strengths (all 2- and 3-piece combos, independent of piece scores)
        self.combo_strengths = {}
        for r in (2, 3):
            for combo in itertools.combinations(PIECES_FOR_COMBOS, r):
                key = "_".join(combo) + "_combo"
                self.combo_strengths[key] = random.randint(0, 100)

        # --- Tactical motifs (shortened set for clarity, you can add full list)
        self.tactics = {
            "fork": random.randint(0, 100),
            "pin": random.randint(0, 100),
            "skewer": random.randint(0, 100),
            "discovered_attack": random.randint(0, 100),
            "sacrifice": random.randint(0, 100),
            "double_check": random.randint(0, 100),
            "deflection": random.randint(0, 100),
            "x_ray_attack": random.randint(0, 100),
            "trapped_piece": random.randint(0, 100),
            "zwischenzug": random.randint(0, 100),
            "clearance": random.randint(0, 100),
            "decoy": random.randint(0, 100),
            "quiet_move": random.randint(0, 100),
            "zugzwang": random.randint(0, 100),
            "passed_pawn": random.randint(0, 100),
            "pawn_storm": random.randint(0, 100),
            "back_rank_mate": random.randint(0, 100),
            "pawn_break": random.randint(0, 100),
            "smothered_mate": random.randint(0, 100),
            "anastasia_mate": random.randint(0, 100),
            "arabian_mate": random.randint(0, 100),
            "boden_mate": random.randint(0, 100),
            "corridor_mate": random.randint(0, 100),
            "double_bishop_mate": random.randint(0, 100),
            "vukovic_mate": random.randint(0, 100),
        }


        # --- Strategic skills
        self.opening_knowledge   = random.randint(0, 100)
        self.middlegame_strategy = random.randint(0, 100)
        self.endgame_strength    = random.randint(0, 100)
        self.evaluation_accuracy = random.randint(0, 100)

        # --- Practical skills
        self.time_management          = random.randint(0, 100)
        self.resourcefulness          = random.randint(0, 100)
        self.psychological_resilience = random.randint(0, 100)
        self.form                     = random.randint(0, 100)

        # --- Psychological traits
        self.risk_taking   = random.randint(0, 100)
        self.confidence    = random.randint(0, 100)
        self.tilt_resistance = random.randint(0, 100)
        self.focus_span    = random.randint(0, 100)
        self.consistency   = random.randint(0, 100)

        # --- Style / play preferences
        self.attack_orientation     = random.randint(0, 100)
        self.defensive_skill        = random.randint(0, 100)
        self.positional_understanding = random.randint(0, 100)
        self.calculation_depth      = random.randint(0, 100)
        self.creativity             = random.randint(0, 100)

        # --- Preparation & knowledge
        self.theoretical_preparation = random.randint(0, 100)
        self.memorization            = random.randint(0, 100)
        self.engine_usage            = random.randint(0, 100)

        # --- Physical & environmental
        self.stamina                 = random.randint(0, 100)
        self.health                  = random.randint(0, 100)
        self.sleep_quality           = random.randint(0, 100)
        self.environmental_adaptation = random.randint(0, 100)

        # --- Career & experience
        self.experience_years    = random.randint(0, 30)
        self.learning_curve      = random.randint(0, 100)

        # --- Derived categorizations
        self.category_scores = self._calculate_category_scores()
        self.primary_category = max(self.category_scores, key=self.category_scores.get)

    def overall_strength(self):
        """Aggregate rating across categories (rough draft weighting)."""
        tactical = sum(self.tactics.values()) / len(self.tactics)
        basic = (self.pawn_strength + self.bishop_strength + self.knight_strength +
                 self.rook_strength + self.queen_strength + self.king_safety_awareness) / 6
        combos = sum(self.combo_strengths.values()) / len(self.combo_strengths)
        strategic = (self.opening_knowledge + self.middlegame_strategy +
                     self.endgame_strength + self.evaluation_accuracy +
                     self.positional_understanding + self.calculation_depth) / 5
        practical = (self.time_management + self.resourcefulness +
                     self.psychological_resilience + self.form) / 4
        psychological = (self.risk_taking + self.confidence +
                         self.tilt_resistance + self.focus_span + self.consistency) / 5
        style = (self.attack_orientation + self.defensive_skill +
                 self.creativity) / 3
        preparation = (self.theoretical_preparation + self.memorization +
                       self.engine_usage) / 3
        physical = (self.stamina + self.health + self.sleep_quality +
                    self.environmental_adaptation) / 4
        career = (self.experience_years * 3) + self.learning_curve

        return round((tactical + basic + combos + strategic + practical +
                      psychological + style + preparation + physical + career) / 10, 2)

    def _calculate_category_scores(self):
        """Group the player's strengths into broad chess skill categories."""
        tactics_average = sum(self.tactics.values()) / len(self.tactics)
        combo_average = sum(self.combo_strengths.values()) / len(self.combo_strengths)
        practical_average = (self.time_management + self.resourcefulness +
                              self.psychological_resilience + self.form) / 4
        psychological_average = (self.risk_taking + self.confidence +
                                  self.tilt_resistance + self.focus_span + self.consistency) / 5
        physical_average = (self.stamina + self.health + self.sleep_quality +
                             self.environmental_adaptation) / 4
        experience_factor = min(100, self.experience_years * 3)
        growth_factor = self.growth_potential
        age_factor = max(0, min(100, 100 - abs(30 - (self.age or 30)) * 2))

        opening_score = (self.opening_knowledge + self.theoretical_preparation +
                          self.memorization + self.engine_usage + self.pawn_strength +
                          self.bishop_strength + self.knight_strength + growth_factor) / 8

        middlegame_score = (self.middlegame_strategy + self.positional_understanding +
                             self.attack_orientation + self.defensive_skill +
                             self.calculation_depth + self.creativity + combo_average +
                             self.evaluation_accuracy) / 8

        endgame_score = (self.endgame_strength + self.king_safety_awareness +
                          self.rook_strength + self.queen_strength + self.resourcefulness +
                          self.psychological_resilience + experience_factor) / 7

        tactics_score = (tactics_average + self.calculation_depth + self.attack_orientation +
                          combo_average + self.creativity) / 5

        other_score = (practical_average + psychological_average + physical_average +
                        self.learning_curve + age_factor) / 5

        return {
            "opening": round(opening_score, 2),
            "middlegame": round(middlegame_score, 2),
            "endgame": round(endgame_score, 2),
            "tactics": round(tactics_score, 2),
            "other": round(other_score, 2),
        }

# Example usage
player = ChessPlayer("All-Rounder", age=28)
print(vars(player))  # show all attributes
print("Overall strength:", player.overall_strength())
