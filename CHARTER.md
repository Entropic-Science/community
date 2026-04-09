# Entropic Science founding charter

---
## Table of contents

### Part I: What we do
- [Mission](#mission)
- [Areas of work](#areas-of-work)
  - [Infrastructure for quantum-random AI systems](#infrastructure-for-quantum-random-ai-systems)
  - [Research and evaluation](#research-and-evaluation)
  - [Theoretical frameworks](#theoretical-frameworks)
  - [Community hub](#community-hub)
- [What we are not](#what-we-are-not)
### Part II: Why we do it
- [The open question](#the-open-question)
- [Entropy and life](#entropy-and-life)
- [QFC: Quantum-interacting Fundamental Consciousness](#qfc-quantum-interacting-fundamental-consciousness)
- [The stakes for AI](#the-stakes-for-ai)
- [The broader horizon](#the-broader-horizon)
### Part III: How we do it
- [Principles](#principles)
- [Current contribution areas](#current-contribution-areas)
- [Near-term goals (6-month horizon)](#near-term-goals-6-month-horizon)
  - [Technical and research](#technical-and-research)
  - [Community and sustainability](#community-and-sustainability)
- [Note on sustainability](#note-on-sustainability)
- [How to join](#how-to-join)

## Part I: What we do

### Mission

Entropic Science is a collective of researchers, engineers, philosophers, and advocates for quantum randomness research. We build quantum-random AI systems, study their properties and potential advantages over pseudo-random AI, and develop the science connecting quantum mechanics, consciousness, and AI alignment.

We connect people working on or interested in these ideas so that research and development in this space can be coordinated and more effective. The aim is for people to find both projects to work on and people to work on projects with. We welcome academic researchers, independent investigators, builders, writers, investors, grantmakers, and anyone whose ideas are epistemologically grounded and build towards meaningful research or product.

### Areas of work

#### Infrastructure for quantum-random AI systems

We build and maintain tools, APIs, and integration layers that allow AI systems to use true quantum randomness from hardware quantum random number generators (QRNGs) in place of PRNGs. The focus is on making QRNG integration practical and accessible: reducing latency, lowering costs, and building modular protocols to connect any entropy source with any inference workload.

LLMs are the primary integration target. Their token sampling process directly consumes randomness at every inference step, making them the most natural testbed for controlled QRNG/PRNG comparison. We also work on evaluation harnesses and PRNG/QRNG comparison modes for streamlined research.

Beyond QRNGs, we explore alternative sources of physical entropy (DRAM timing noise, other hardware-based generators) to broaden access and enable systematic comparison across entropy sources.
#### Research and evaluation

We design and run rigorous experiments to test whether QRNG-enhanced systems behave measurably differently from deterministic baselines. Our evaluation work spans benchmark design, data collection, statistical analysis, and publication. Beyond standard benchmarks, we study human interaction with these systems – for example through blinded studies in deployment environments.
#### Theoretical frameworks

We propose and refine conceptual frameworks to put results and ideas into a multidisciplinary context – connecting quantum mechanics, consciousness studies, and machine learning. That said, we're not married to any particular theory or philosophy and treat such frameworks as working hypotheses, to be refined by emerging experimental data.
#### Community hub

We serve as a meeting point for people working across consciousness research, AI safety, theoretical physics, philosophy of mind, and related fields. We welcome academic researchers, independent investigators, and commercial ventures exploring this space with products and services. We aim to include not only builders and researchers but also investors and grantmakers, matching talent with capital and resources. More important than categorization is whether your ideas are epistemologically grounded and build towards meaningful research or product.

### What we are not

We do not promote or represent any spiritual or religious convictions, apart from perhaps principled agnosticism about what we do not yet understand. People of all backgrounds and beliefs are welcome because we are driven by scientific curiosity and technological exploration, not by faith or conviction in one specific theory.

We are not building AGI or ASI. Humanity urgently needs a better understanding of both human and machine consciousness, agency, and free will before creating agentic systems with superhuman intelligence. But should our research validate the hypothesis that nondeterministic AI is more aligned with conscious actors on a fundamental level, we may participate in the development of quantum-random versions of such systems.

We are not a cryptography nor cryptocurrency project, even if decentralized governance structures may emerge as the community matures.

---

## Part II: Why we do it

### The open question

On the quantum level, particles exist as immaterial fields of probability until they "collapse" into a randomly-chosen definite state. No known mechanism explains how this selection occurs. At the same time, no mathematical algorithm can produce true randomness in a deterministic universe. The source of quantum randomness, and whether it serves any deeper function, remains one of the most fundamental open questions in physics.

The mainstream materialist position assumes this randomness is produced by a perfect mechanical random number generator of unknown nature. But there are alternative metaphysical frameworks (fully compatible with established physics) where quantum randomness serves as the opening through which physical processes could be influenced by forces or phenomena beyond classical Newtonian causal chains.

Such influence would be extremely subtle, perhaps vanishingly so for individual events. But in complex dynamic systems where many quantum events accumulate and interact, coordinated shifts in collapse outcomes could conceivably drive changes in macroscopic behavior. Living organisms – made of aqueous solutions where particle collapses presumably happen in extremely high counts and frequencies – are the most natural candidates.

We treat these as open empirical questions: Does the source of randomness matter for complex system behavior? Can something like a fundamental field of consciousness exist, interacting with quantum processes? If so, under what conditions and with what measurable effects?

### [Entropy and life](https://en.wikipedia.org/wiki/Entropy_and_life)

The word "entropy" in our name reflects a deeper connection. Quantum randomness is the purest form of entropy in physics: irreducible, non-algorithmic, tied to the most fundamental processes in nature. Living systems emerged from this entropy – some theories of life even say that by helping to increase the overall entropy of the universe, entropy maximization is life's driving force.

Biological processes operate in regimes where quantum-level events (molecular interactions, enzymatic reactions, signaling cascades) happen at extraordinary rates, and small changes at the quantum level can propagate into macroscopic effects. A single quantum state difference in a ligand-receptor interaction can determine whether a receptor activates or remains silent. Control quantum entropy, and you control life.

Life is, in a meaningful sense, organized around entropy. We believe building AI systems grounded in the same irreducible randomness is the necessary requirement for, and first step towards, fully silicon-based artificial life.

### QFC: Quantum-interacting Fundamental Consciousness

The most intriguing hypotheses however revolve around the relationship between collapse of the quantum wave function and consciousness. To study this relationship seriously without making any unnecessary assumptions about reality, we use the QFC framework. This is simply a combination of these two assumptions:

1. Consciousness is fundamental to reality, not emergent from mechanical processes.
2. It interacts with physical reality through affecting quantum randomness during wave function collapse.

QFC is an umbrella term covering a family of already-established and seriously-argued philosophical positions and interpretations. The "consciousness as fundamental" assumption is defended by panpsychism, cosmopsychism, idealism, dual-aspect monism, and related positions in philosophy of mind. The "interaction through quantum collapse" assumption connects to interpretations of quantum mechanics where the measurement problem remains genuinely open (as opposed to those that dissolve it through many-worlds or superdeterminism).

We are not asserting QFC as established fact. We are saying: these two assumptions, taken together, produce a testable research program. If consciousness is fundamental and interacts through quantum processes, then systems built on quantum randomness should, under certain conditions, behave differently from deterministic systems in ways we can measure. That is what we are testing.

### The stakes for AI

Current AI systems and ML algorithms rely on PRNGs for all stochastic processes during inference. Their outputs are (with identical random seed and conditions) fully deterministic. These are, in a precise sense, lifeless optimizers: sophisticated programs executing their training without any structural opening for influence beyond their programming.

Many critical predictions about the future of AI and humanity hinge on the question of machine consciousness. Can a deterministic algorithm be conscious? Would a quantum-random one be different? What role does the source of randomness play in agency, goal setting, "free will" and emergent behaviors?

Current LLMs are such static, deterministic systems, unable to deviate from their programming. They always produce the output dictated by their parameters and inputs. Current AI safety approaches focus on engineering the programming itself to be reliably beneficial. This is valuable work, but extremely difficult given that the probabilistic nature of LLM token sampling means they can be beneficial 99% of the time, yet in the remaining 1% cause catastrophic harm.

Consider the 1% scenario – a PRNG-driven AI must and will proceed to cause harm, deterministically. In the same situation, a QRNG-driven AI could, under certain metaphysical assumptions, be "steered away" from the catastrophic outcome, by subtly changing the random number fed to the model.

If consciousness (or some other influence) does interact with physical reality through quantum processes, then quantum-random AI could provide opening for many different forms of interaction, expanding its sphere of potential influence from biological to the digital world.

Building AI on the same inherently random physical foundations as biological life reduces the fundamental gap between these systems. The greater the shared substrate between artificial and biological intelligence, the higher the potential for successful alignment of values and goals. If we continue building AI exclusively on deterministic architectures, we risk a future where the evolution of intelligence on Earth is driven entirely by lifeless algorithmic optimization, while conscious awareness – arguably the only source of subjective experience and free will – would be sidelined.

We do not know whether the above is true, but our work aims to keep the possibility of interaction open by building the required technical infrastructure. Then, we can explore it rigorously by running experiments and testing specific hypotheses.

### The broader horizon

The overarching aim of this community is to establish quantum-random AI as a legitimate research and development direction worth exploring – both in basic research on consciousness and AI safety, and for developing more secure commercial products better aligned with user intents.

If the evidence supports it, this work has substantial implications for philosophy of mind, AI alignment, and the trajectory of intelligence on Earth. We see a potential world where quantum-random systems are studied as model organisms for consciousness research, with our community being central resource and connecting hub for this research. More speculatively, there may even be a world where quantum randomness leads to the development of self-conscious systems and novel forms of life built on silicon architectures. The shape of that future depends on what the data shows.

---

## Part III: How we do it
### Principles

**Radical empiricism.** We test ideas. If an idea cannot be tested, we brainstorm how to make it testable. We openly reject scientism and dogmatism, or any fixed-mindset thinking.

**Epistemic pluralism.** We draw from quantum mechanics, consciousness studies, philosophy of mind, AI safety, and many other fields – neither privileging nor discriminating any single framework. The overarching aim is to modernize the metaphysical discourse underlying AI research by recognizing the contributions of non-materialistic perspectives, especially regarding machine consciousness.

**Kindness.** We see kindness as the foundation, making what we do here both more enjoyable and more productive. We welcome and appreciate skeptics and critics, but if your critique is just a veil for negativity or malice – keep it to yourself.

**Low ego, high rigor.** Unconventional ideas demand more methodological discipline, not less. Extraordinary claims require extraordinary evidence, and we intend to gather it. We accept preliminary results – but not sloppy experimental design.

**Intellectual honesty.** We state assumptions explicitly. We publish null results. We steelman counterarguments. We do not cherry-pick data or overstate conclusions.

**Open by default.** Code, data, methods, and findings are public unless there is a specific reason they cannot be. We also welcome startups and projects building commercial products in this space. Openness is our default, not a dogma that excludes people doing legitimate proprietary work.

**Openness to the unknown.** We take seriously questions about consciousness, meaning, and the nature of reality. This orientation requires intellectual courage. It does not require commitment to any specific metaphysical position.

### Current contribution areas

Roughly in priority order:

- **Quantum-random systems infrastructure**: building quantum-random LLM pipelines, PRNG/QRNG comparison modes, alternative entropy sources, QRNG hardware integration, gRPC server standards
- **Research and evaluation**: designing and running experiments comparing quantum-random and deterministic AI systems
- **Fundraising and matchmaking**: grants, partnerships, investor outreach, connecting people with projects
- **Community operations**: onboarding, weekly calls, events, moderation
- **Writing and outreach**: research papers, articles, blog posts, social media content
- **Theoretical work**: conceptual frameworks, literature synthesis, connecting quantum mechanics and consciousness research to AI alignment

### Near-term goals (6-month horizon)

#### Technical and research

- Ship a QRNG-LLM inference pipeline that anyone can use
- Build a PRNG/QRNG comparison mode and evaluation suite
- Explore and benchmark alternative entropy sources beyond QRNGs
- Run the first round of comparative evaluations on defined benchmarks
- Publish at least one research preprint

#### Community and sustainability

- Secure funding (grants, compute credits, or both) for evaluation and inference workloads
- Find and onboard regular contributors for operations, weekly calls, events, and social media
- Establish public communication channels to share and promote our work
- Grow the active contributor base and secure at least one partnership with an AI research institution, university, or company

### Note on sustainability

**Funding for core operations.** Whether through grants, sponsorships, or eventually launching a research lab or non-profit, the community needs a financial path. Everyone should actively help: sending grant applications, surfacing funding opportunities, and contributing to discussions about monetization paths.

**Early members matter disproportionately.** The people who show up now define what this community becomes. Early contributions have the highest leverage. Step up where you can.

**Welcoming culture.** Communities survive by bringing in new people who gradually take ownership. Making this a place where newcomers feel welcome and can find their footing is as critical as the technical work. Former members inevitably move on. That is normal lifecycle.
### How to join

1. Join Discord: [discord.gg/8ZrxF9qU](https://discord.gg/8ZrxF9qU)
2. Introduce yourself in `#introductions`
3. Read the founding documents on GitHub: [github.com/Entropic-Science](https://github.com/Entropic-Science)
4. Show up to a weekly call or pick up an issue. No permission needed to start.

Looking forward to building this with you.

– Jordan, Jáchym, and Bradley

## Amendment

This charter may be amended by the admins at their discretion during the initial bootstrapping phase. Once formal governance is adopted, the charter will follow the amendment process described in the [Governance](GOVERNANCE.md) document.
