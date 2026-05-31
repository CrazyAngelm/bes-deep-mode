# Original Research: Self-Improving Language Models with Bidirectional Evolutionary Search

This repository packages a practical agent skill inspired by the original BES research:

- Project page: <https://guoweixu.com/bes/>
- Paper: <https://arxiv.org/abs/2605.28814>
- Code: <https://github.com/Embodied-Minds-Lab/BES>

## Citation

```bibtex
@misc{xu2026selfimprovinglanguagemodelsbidirectional,
      title={Self-Improving Language Models with Bidirectional Evolutionary Search},
      author={Guowei Xu and Zhenting Qi and Huangyuan Su and Weirui Ye and Himabindu Lakkaraju and Sham M. Kakade and Yilun Du},
      year={2026},
      eprint={2605.28814},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.28814},
}
```

## What BES contributes

Bidirectional Evolutionary Search (BES) couples two processes:

1. **Forward candidate evolution**: standard expansion plus evolutionary operators that recombine and edit partial trajectories.
2. **Backward goal decomposition**: recursive decomposition of the original task into checkable sub-goals that provide dense intermediate feedback.

The project page summarizes the motivation: best-of-N sampling and tree search are limited by sparse verification signals and by expansion from high-probability model regions. BES adds evolutionary operators to escape expansion-only search regions and backward decomposition to provide denser feedback.

## Forward search operators

The original BES method describes five forward operators:

- **Expansion**: the policy generates new steps.
- **Combination**: two trajectories sharing a common prefix concatenate their distinct suffixes.
- **Deletion**: an interior step is removed.
- **Translocation**: a step in one path is replaced by a step from another path.
- **Crossover**: one path is cut at a splice point and its tail is replaced by another path's tail.

## Backward search

Backward search decomposes the problem into a tree of fine-grained sub-goals. Forward nodes are scored against that tree: candidates that address more sub-goals receive higher scores, even before fully solving the task.

## Reported benchmark results

The benchmark numbers below are copied from the BES project page on 2026-05-31. Higher is better unless noted.

### Multi-hop reasoning post-training: MuSiQue

| Backbone | Method | Accuracy (EM) | Delta vs base | # Valid Search | # Valid Actions | Finish Ratio |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Llama-3.2-3B | Base | 4.0 | — | — | — | — |
| Llama-3.2-3B | GRPO | 2.1 | -1.9 | 0.84 | 0.20 | 0.64 |
| Llama-3.2-3B | Tree-GRPO | 3.9 | -0.1 | 1.50 | 2.14 | 0.64 |
| Llama-3.2-3B | BES | 7.0 | +3.0 | 2.31 | 3.29 | 0.97 |
| Llama-3.1-8B | Base | 6.6 | — | — | — | — |
| Llama-3.1-8B | GRPO | 5.6 | -1.0 | 1.46 | 1.83 | 0.37 |
| Llama-3.1-8B | Tree-GRPO | 7.4 | +0.8 | 0.65 | 1.36 | 0.71 |
| Llama-3.1-8B | BES | 10.4 | +3.8 | 2.11 | 3.05 | 0.94 |

### Open problem solving with GPT-5 backbone

Reported format: mean ± std over 3 seeds / best.

| Method | Circle Packing (Square, n=26) | Circle Packing (Rectangle, n=21) | Heilbronn (Convex, n=13) |
| --- | ---: | ---: | ---: |
| Human | — / 2.634 | — / 2.364 | — / 0.0306 |
| AlphaEvolve | — / 2.635 | — / 2.3658 | — / 0.0309 |
| OpenEvolve | 2.531 ± .018 / 2.541 | 2.267 ± .014 / 2.276 | 0.025 ± .005 / 0.027 |
| GEPA | 2.613 ± .022 / 2.628 | 2.326 ± .023 / 2.354 | 0.025 ± .002 / 0.027 |
| ShinkaEvolve | 2.464 ± .083 / 2.541 | 2.335 ± .026 / 2.358 | 0.023 ± .005 / 0.026 |
| BES | 2.623 ± .014 / 2.632 | 2.349 ± .012 / 2.360 | 0.026 ± .001 / 0.027 |

## Relationship to this skill

`skill/SKILL.md` is not a full reproduction of the BES algorithm. It adapts the paper's core discipline into a lightweight agent skill:

- generate multiple forward candidate plans;
- reason backward from desired final state and verification evidence;
- recombine the strongest plan fragments;
- score the result before acting;
- run bounded self-review after execution.

The optional local `bes_runner` notes in this repository describe how an agent host can expose that loop as deterministic structure, while leaving actual reasoning and verification to the agent and its tools.

## Limitations

- This repository does not include the original BES training or inference code; use the upstream code repository for that.
- The skill is a practical adaptation for agent workflows, not a benchmark reproduction.
- Benchmark results are cited from the project page and should be verified against the paper/code before being used in formal claims.
