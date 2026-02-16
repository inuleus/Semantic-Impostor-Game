# Semantic Impostor Game
A Python social game exploring linguistic associations and deception. Features a modular structure and cross-platform command line interface.

# Project Background
- *Linguistic Mechanisms*. This game utilizes the concepts of semantic priming and linguistic competition. The same word is assigned to all players but one; the impostor receives instead a clue which consists of a semantically related word.
- *Gameplay dynamics*. Players take turns saying words related to the target one. The game consists of choosing words that are specific enough to be recognized by other players but vague enough not to give too many clues to the impostor on what the correct target is.
- *Win Conditions*. If the impostor is found after a set number of rounds, the other players win. If a player is falsely accused of being the impostor, they lose. This set-up allows us to explore the boundaries of semantic relations between nouns.

# Main Features
- *Dynamic Loading*. Pairs of word-clue are dynamically loaded from a text file.
- *Modular Architecture*. The game is structured in a modular fashion. This allows us to reuse the same structure to play other games or to play the same game with different corpora of word-clue (e.g., in a different language).
- *Prtability*. The game is portable: it works on different operating systems.

# Accessibility and UX
- *Data Privacy*. The function clearScreen() allows for the privacy needed to play the game in group set-ups. After being printed on the terminal, information is erased to ensure that the target word stays secret.
- *Inclusivity*. Vertical space between text lines has been implemented (by using the character \n) to improve readability for users with dyslexia.

# How to use: structure of the files
- *Source code*. The file 'semantic_game.py' contains the code implementing the game itself.
- *Word Database*. The file 'corpus.txt' contains an already correctly formatted list of words and clues.
