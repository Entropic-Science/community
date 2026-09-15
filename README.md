# Entropic Science

An open research collective building quantum-random AI systems, studying their properties and potential advantages over pseudo-random AI, and advancing the scientific understanding of quantum randomness, consciousness, and their implications for AI alignment.

**Website**: [entropic.science](https://entropic.science)
**GitHub**: [github.com/Entropic-Science](https://github.com/Entropic-Science)
**Discord**: [discord.gg/2EbveaB2wS](https://discord.gg/2EbveaB2wS)

## The mission

Every AI system running today relies on pseudo-random number generators (PRNGs) for its stochastic processes. Controlled for the random seed, these systems are fully deterministic. The randomness in quantum mechanics is fundamentally different: no known mechanism, algorithm, or hidden variable can account for how a quantum particle "chooses" its definite state upon measurement. This remains one of the deepest open questions in physics.

Entropic Science exists to investigate what happens when AI systems are built on true quantum randomness instead. We build the infrastructure to make this possible, run experiments to test whether and how it matters, and develop theoretical frameworks connecting quantum mechanics, consciousness, and AI alignment.

Each of us cares about this for different reasons – from understanding the ultimate nature of consciousness to aligning powerful AI systems. But increasingly powerful deterministic AI systems are shaping the trajectory of our civilization, which makes AI the most urgent place to look. If the source of randomness has any bearing on how these systems behave, on whether they can be meaningfully aligned with conscious beings, or on the deeper relationship between computation and consciousness, we want to find out – while we still have a choice about how AI is built.

### What we do

**Infrastructure.** We build tools, APIs, and integration layers that allow AI systems (especially LLMs) to use hardware quantum random number generators (QRNGs) in place of PRNGs. This includes low-latency QRNG pipelines, gRPC server standards, and modular protocols connecting any entropy source to any inference workload. We also explore alternative sources of physical entropy (DRAM timing noise, other hardware generators) for more accessible quantum randomness.

**Research and evaluation.** We design and run experiments testing whether QRNG-enhanced systems behave measurably differently from deterministic baselines. Beyond standard benchmarks, we study human interaction with these systems – for example through blinded studies in deployment environments.

**Theoretical work.** We facilitate debates with people from various fields to develop conceptual frameworks connecting quantum mechanics, consciousness research, and AI alignment. We treat these as working hypotheses refined by emerging experimental data.

**Community.** We connect researchers, builders, philosophers, investors, and grantmakers working on or interested in these questions. The aim is to coordinate research and development that would be difficult alone: finding projects to work on, people to work with, and matching talent with capital and resources.

### Why quantum entropy

Quantum randomness is the one point in physics where the outcome of a physical process is, as far as we can tell, genuinely undetermined. Under several serious philosophical frameworks (fully compatible with established physics), this indeterminacy represents the opening through which consciousness, agency, or other phenomena beyond deterministic causal chains could have causal influence over physical matter. In any case, such influence would be extremely subtle for individual events. But in complex systems where many quantum events accumulate and interact, coordinated shifts could conceivably drive macroscopic effects. Living organisms, made up of aqueous environments with extremely high rates of quantum collapse events, are the most natural candidates.

We take this possibility seriously and investigate it empirically, without asserting it as fact. The question "does the source of randomness matter for complex system behavior?" is testable, and the answer could reshape our understanding of consciousness, technology, and the future of AI. Implications for AI alignment are of particular interest given the fast pace of progress in AI capabilities.

Building AI systems on the same inherently random physical foundations as life itself reduces the fundamental gap between artificial and biological intelligence. The greater the shared substrate, the higher the potential for meaningful alignment between human values and machine behavior. If consciousness does interact with quantum processes, then quantum-random AI could be the first artificial system amenable to that interaction.

The full reasoning, research agenda, and philosophical context are in the [Charter](CHARTER.md).

## Quick start

1. **Join Discord**: [discord.gg/2EbveaB2wS](https://discord.gg/2EbveaB2wS)
2. **Introduce yourself** in `#introductions`
3. **Read** [How we work](HOW_WE_WORK.md) to understand our tools and processes
4. **Start contributing**: see [Contributing guide](CONTRIBUTING.md)

## Documents

| Document | Contents |
|----------|----------|
| [Charter](CHARTER.md) | Mission, scope, motivations, principles, goals |
| [Code of conduct](CODE_OF_CONDUCT.md) | Behavioral standards and enforcement |
| [How we work](HOW_WE_WORK.md) | Tools, communication, task tracking |
| [Contributing guide](CONTRIBUTING.md) | How to participate and division scopes |

## Active projects

| Project | Description |
|---------|-------------|
| [qr-sampler](https://github.com/Entropic-Science/qr-sampler) | Integrate any source of randomness into LLM token sampling — modular profiles for inference engines, entropy sources, sampling methods |
| [knowledge-base](https://github.com/Entropic-Science/knowledge-base) | Central knowledge base — shared library, division boards (rosters, proposals, active projects) |

## Divisions

| Division | Scope |
| --- | --- |
| Infrastructure | Quantum-random LLM inference pipelines, QRNG hardware integration, alternative entropy sources, gRPC server standards, PRNG/QRNG comparison modes, evaluation harnesses |
| Research | Experimental design, benchmarks and evaluation suites, statistical analysis, theoretical frameworks, literature synthesis, philosophy of mind, AI alignment theory, publications |
| Outreach-Fundraising | Grant applications, partnerships, investor outreach, social media, articles, events, onboarding, community operations |

Each division has a roster, proposals page, and active projects list in the [knowledge base](https://github.com/Entropic-Science/knowledge-base).

## Tools

| Tool | Purpose |
|------|---------|
| [Discord](https://discord.gg/2EbveaB2wS) | Real-time discussion, voice calls, coordination |
| [GitHub Projects](https://github.com/orgs/Entropic-Science/projects) | Task boards, backlog, issue tracking |
| [Knowledge base](https://github.com/Entropic-Science/knowledge-base) | Shared research, project docs, division rosters and proposals |

## Administration

This community is currently administered by its three founders:

| Admin | Handle |
|-------|--------|
| Jordan McKinney | @jordanmmck |
| Jáchym Fibír | @kluck77 |
| Bradley Stephenson | @orphiceye |

Formal governance structures (steering council, decision-making tiers, division leads) are being developed and will be published as a separate Governance document when ready.

## Licensing (unless stated otherwise)

Code: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
Research and content: [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Contact

Email: [hello@entropic.science](mailto:hello@entropic.science)
Website: [entropic.science](https://entropic.science)
Discord: [discord.gg/2EbveaB2wS](https://discord.gg/2EbveaB2wS)
