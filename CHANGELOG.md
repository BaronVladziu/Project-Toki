## Entry Structure

```
## [MAJOR.MINOR.PATCH] - YEAR-MONTH-DAY
### Added
### Changed
### Removed
### Fixed
```

More info here: https://semver.org/


## [0.0.27] - 2026-01-07

### Added

- support for `mi` and `sina` subjects in `Grammar` class
- support for `NOUN_PHRASE` objects in `Grammar` class


## [0.0.26] - 2025-12-23

### Added

- support for noun phrases in `Grammar` class


## [0.0.25] - 2025-12-21

### Added

- support for simple `X li X` sentences in `Grammar` class


## [0.0.24] - 2025-12-17

### Added

- new getters to `Dictionary` class
- loading words from `dictionary_data.json` in `Grammar` class


## [0.0.23] - 2025-12-16

### Added

- separation to subsentences in `Grammar` class
- `ADJECTIVE_PHRASE` definition to `Grammar` class

### Changed

- renamed `grammar_parser_test.py` to `grammar_test.py`


## [0.0.22] - 2025-12-15

### Changed

- fixed `PREVERB` spelling
- private nodes to use Lark built-in feature


## [0.0.21] - 2025-12-13

### Added

- support for private node names in `GrammarParser`


## [0.0.20] - 2025-12-11

### Added

- support for complex node names in `GrammarParser`


## [0.0.19] - 2025-12-10

### Added

- separation to sentences in `Grammar` class
- support for punctuation in `GrammarParser` class


## [0.0.18] - 2025-12-07

### Added

- unknown word support for `Grammar` class


## [0.0.17] - 2025-12-05

### Added

- `GrammarParser` class


## [0.0.16] - 2025-12-04

### Added

- `Grammar` class

### Changed

- `pre-commit` version to `4.5.0`


## [0.0.15] - 2025-12-01

### Added

- `isort` to `pre-commit`


## [0.0.14] - 2025-11-30

### Added

- `Phrase` class


## [0.0.13] - 2025-11-28

### Added

- `Dictionary` class


## [0.0.12] - 2025-11-26

### Changed

- prettify tests


## [0.0.11] - 2025-11-24

### Added

- tests for `Word` and `Punctuation` classes


## [0.0.10] - 2025-11-23

### Added

- `PartOfSpeech` variable to `Word` class


## [0.0.9] - 2025-11-21

### Added

- code coverage


## [0.0.8] - 2025-11-20

### Changed

- simplify `PartOfSpeech` class


## [0.0.7] - 2025-11-19

### Added

- `PartOfSpeech` class


## [0.0.6] - 2025-11-12

### Added

- `Punctuation` and `Text` classes

### Removed

- `rich` library since it's unused


## [0.0.5] - 2025-11-11

### Added

- `black` to `pre-commit`

### Removed

- `reorder-python-imports` from `pre-commit`


## [0.0.4] - 2025-11-10

### Added

- `dictionary_data.json` with nimi ku suli


## [0.0.3] - 2025-11-06

### Added

- `Word` class


## [0.0.2] - 2025-11-04

### Added

- Pre-commit


## [0.0.1] - 2025-11-03

### Added

- Virtualenv building script
