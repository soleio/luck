# The Geometry of Luck: Theory

This file contains the conceptual foundation for the operational diagnostic in [luck.md](luck.md). It is written for human readers and for anyone who wants to evaluate, extend, or attack the framework. You do not need it to run the diagnostic.

-----

## Core Premise

The universe does not select for complexity in the abstract. It selects for complexity that can sustain its own pattern against dissipation. An assembly that cannot harness enough energy to hold itself together disappears regardless of its elegance. An invasive species that collapses the ecology sustaining it perishes with it. This is true of molecules, organisms, institutions, and markets -- the principle is thermodynamic before it is economic.

But persistence alone does not explain why complexity increases. The direction of complexity is toward configurations that increase their own metabolic throughput through ecological coupling -- and this process has a hierarchy. Individual assemblies must be solvent. Solvent assemblies couple to gradients. Coupling creates structures through which energy and capability circulate. Circulation sustains integration across systems. And integration density determines the assembly index an ecology can reach. Bands of tribes with a common language are not a civilization. Bands of tribes connected by trade routes, political pacts, legal codes, and shared infrastructure are -- because each integration structure increases the total throughput of the network, generating the surplus that makes the next integration structure possible.

Complexity does not produce integration. Integration produces complexity. The arrow of desire -- the tendency of solvent systems to evolve toward greater ecological throughput through deeper coupling -- traces this path.

### On the word "luck"

This framework uses "luck" as a *defined term*, not a metaphysical discovery. We define luck as the rate at which an agent increases the throughput, circulation, and integration of the systems it participates in -- a vector with direction and magnitude, not an outcome one receives. The claim being made is pragmatic: that the cluster of properties this definition picks out (surplus capacity, gradient diversity, circulation rate, integration density, niche construction) predicts persistence and compounding better than the colloquial notion of luck-as-randomness, and better than single-variable alternatives. That claim is testable, and the Measurement section below states what would falsify it. Readers who prefer to mentally substitute "structural fortune" or "persistence capacity" for "luck" lose nothing.

-----

## Extended Worked Examples

### Low assembly, high compatibility, no niche construction

A political meme -- an image macro juxtaposing a public figure with a situational caption. Assembly index is minimal: one image, one cultural reference, one comedic frame. Reconstruction cost is near zero, so it spreads instantly. But it constructs no niche. It cannot generate demand for itself beyond the initial context. Its gradient (topical attention) is non-renewing. Diagnosis: flash in the pan. The structural fortune is entirely positional -- the right node in the right network at the right moment. The luck is real but non-compounding.

### High assembly, self-sustaining, niche-constructing

The U.S. Constitution. Assembly index is enormous -- it requires prior assembly of English common law, Enlightenment philosophy, colonial governance experience, the specific failures of the Articles of Confederation, and political compromises among competing factions. But it exhibits the self-sustaining property: it creates courts, legislatures, amendment processes, and legal pedagogy that generate continuous demand for constitutional interpretation. Each successful governance outcome reinforces the institutional ecology. Gradient pluralism is strong -- it couples to legal, political, educational, and cultural throughput simultaneously. Its luck compounds structurally.

A retrodiction the framework offers (a post-hoc reading, not a prediction -- see the note on retrodiction below): constitutions of comparable intellectual quality, such as Weimar Germany's or various post-colonial constitutions, failed not because the ideas were worse but because the surrounding assembly ecology could not sustain their persistence -- the gradient coupling or institutional niche construction was insufficient. This reading is consistent with the framework; it is not evidence for it. Evidence would require the kind of out-of-sample tests described under Measurement.

### Integration as the threshold of civilization

Bands of tribes may share language, sophisticated tool-making, social hierarchy, and deep ecological knowledge. The assembly index within each tribe can be substantial. But each tribe is a closed circulatory system -- knowledge, resources, and capability flow within it but not between tribes in any structured way. Common language lowers the cost of coupling but does not create the structures of coupling. Two tribes that can talk are not integrated. Two tribes connected by a trade route they both depend on and maintain are the beginning of integration. Add a shared grazing agreement, a marriage alliance with kin obligations, a seasonal gathering with rituals neither group can perform alone -- each is a circulatory structure through which throughput flows between systems. Each one, once established, lowers the cost of the next. A trade route creates conditions for a trade agreement. A trade agreement creates conditions for standardized measures. Standardized measures create conditions for taxation. Taxation creates conditions for infrastructure. Infrastructure creates conditions for law. This is the arrow of desire operating at the inter-system level: each integration structure increases total throughput, generating the surplus that makes the next structure possible. The civilization's assembly index emerges from the density of circulatory connections between its parts.

### Circulation failure: empires that collapse from the edges

Empires do not fail from their center. They thin at the periphery. Roads are maintained less, garrisons supplied less, local officials supervised less. The circulation structures go quiet. Without active flow, the integration at the edges decays, and the periphery reverts to the assembly index it can sustain on its own -- the region, the tribe, the local chieftain. The most fragile point was never the most complex assembly (the capital, the court, the legal code). It was the most critical circulatory bottleneck -- the road, the supply line, the communication channel that kept the periphery coupled to the whole.

### The reflexive case: this framework

This skill is itself an assembly entering an ecology. Its solvency depends on whether it produces measurably better outputs when used -- if it does, it sustains continued attention; the eval harness in `evals/` exists to test exactly this. Its gradient coupling targets AI-assisted decision-making, a renewing and expanding flow. Its compatibility is designed to be high: it follows existing skill-file conventions and uses a sequential checklist with explicit anchors that requires no prior theoretical knowledge. Its niche construction bet is that the vocabulary (solvency, circulation, integration density, binding constraint) becomes useful shorthand that creates demand for the framework itself. Its circulation test: does the framework flow outward from this document into other contexts -- conversations, decisions, designs -- and return as improved practice and contributed examples? Its integration test: does it connect domains that were previously siloed -- thermodynamics and strategy, ecology and business, physics and fortune?

-----

## A Note on Retrodiction

Every worked example above is a retrodiction: a historical case read through the framework after the outcome is known. Retrodictions demonstrate that the framework can be *applied*; they do not demonstrate that it *predicts*. Any sufficiently flexible framework can accommodate known outcomes. The framework's claim to be more than generic strategy advice rests entirely on the predictions below and on prospective use -- diagnoses made before outcomes are known, recorded, and scored. Users who want to contribute evidence should record diagnoses at decision time (the `examples/` directory shows the format) and revisit them.

-----

## Measurement and Falsifiability

The framework makes testable predictions that distinguish it from generic strategy advice.

**Prediction 1: Solvency dominates.** Among artifacts with comparable assembly indices, those with higher surplus capacity will show longer persistence and wider adoption than those with stronger gradient coupling but thinner margins. Test via: startup survival data correlated with burn rate vs. market size; open-source project longevity correlated with maintainer capacity vs. GitHub stars; ecosystem persistence correlated with net energy surplus vs. species diversity.

**Prediction 2: Metabolic reach predicts resilience.** Artifacts coupled to more independent gradients should survive single-gradient shocks at higher rates, with survival probability increasing monotonically in the number of independent gradients. (We state the monotonic form only. A precise functional form would require assumptions -- equal gradient sizes, independent shocks -- that real systems violate; deriving the shape of the curve under realistic assumptions is open work.) Test via: company survival rates after industry disruptions, correlated with revenue stream diversity.

**Prediction 3: Niche construction separates compounding from linear growth.** Artifacts exhibiting niche construction (adoption creates further demand) should show accelerating influence curves (superlinear growth), while those without should show linear or decelerating curves. Test via: technology adoption S-curves segmented by presence/absence of ecosystem effects.

**Prediction 4: Circulation rate predicts system health better than aggregate throughput.** Systems with high total throughput but low circulation (pooled resources, stagnant flow) should show higher fragility and faster decline than systems with lower total throughput but active circulation. Test via: economic resilience correlated with velocity of money rather than GDP; ecosystem resilience correlated with nutrient cycling rate rather than total biomass.

**Prediction 5: Integration density predicts maximum achievable assembly index.** The most complex artifacts in any domain should emerge from the most densely integrated ecologies, not from the most individually capable agents. Test via: patent complexity correlated with regional collaboration density; species complexity correlated with ecosystem interconnectedness; cultural output correlated with trade network density.

**Prediction 6: Failure mode classification is diagnostic.** The named failure modes should be recoverable from observable data (growth rate, retention rate, adoption breadth, gradient diversity, circulation velocity, network density, ecosystem dependency) via unsupervised clustering, without foreknowledge of the framework. If the clusters emerge independently, the taxonomy reflects real structure rather than imposed categories. (Note: the taxonomy is explicitly non-exhaustive -- it names recurring attractor states, not a partition of the facet space. The prediction is that these seven appear as distinct clusters, not that no other clusters exist.)

**Prediction 7 (reflexive): The skill improves outputs.** Responses to strategic-decision prompts generated with this skill loaded should be preferred by blinded judges over responses generated without it, on the criteria in `evals/judge-rubric.md`. This is the cheapest prediction to test and the one this repository is directly accountable for. The eval harness in `evals/` implements it.

**What would falsify this framework:** If surplus capacity, metabolic reach, circulation rate, integration density, and niche construction show no predictive advantage over simpler single-variable models (e.g., raw market size, or random timing), then the framework's added complexity is not earning its keep -- and by its own logic is insolvent. Likewise, if Prediction 7 fails -- if the skill does not produce preferred outputs -- the framework's reflexive solvency claim fails regardless of its theoretical appeal.

-----

## Theoretical Grounding

This framework extends Assembly Theory, which proposes that the assembly index -- the minimum number of joining operations needed to construct an object -- distinguishes objects requiring selection and history from those that don't. Objects above a threshold assembly index are evidence of evolutionary or technological selection processes. Key papers: Marshall et al., "Identifying molecules as biosignatures with assembly theory and mass spectrometry" (*Nature Communications*, 2021); Sharma et al., "Assembly theory explains and quantifies selection and evolution" (*Nature*, 2023).

**Assembly Theory is contested.** Published critiques argue that the assembly index is formally equivalent or near-equivalent to existing compression and complexity measures, and that the theory's claims about selection are not as novel as presented. This framework does not depend on Assembly Theory winning those disputes: it borrows the *vocabulary* (assembly index, joining operations, selection history) as a lens, and its own claims stand or fall on the predictions in the Measurement section, not on the status of assembly theory in chemistry. Readers should treat the grounding as a source of structure, not of proof.

The extension this framework proposes: assembly index alone does not predict persistence, and it is not a prime mover. What persists is what can sustain its own continuation within the ecology of other assemblies it depends on. And what ascends in complexity does so because integration density -- the circulatory interconnection of an ecology's parts -- creates the conditions for higher-order assembly. Complexity is downstream of integration, not the reverse.

Adjacent theoretical resources:

- **Dissipative adaptation** (England, 2013): thermodynamic basis for self-organizing structures that absorb and dissipate environmental energy. This framework adds an ecological constraint: dissipative structures that degrade their own gradient sources collapse, while those that enrich or maintain them ascend.
- **Free energy principle** (Friston, 2010): directed exploration as surprise minimization; formalizes the "desire" gradient as prediction-error reduction.
- **The adjacent possible** (Kauffman, 1996): the expanding frontier of achievable assembly states; each successful assembly opens new combinatorial territory. This framework specifies that the adjacent possible expands primarily through integration, not through individual complexity.
- **Niche construction theory** (Odling-Smee et al., 2003): organisms modify their own selective environments, creating inheritance channels beyond genetics.

The geometry is this: the space of possible assemblies has a topology shaped by mutual solvency and integration density. The viable region is where your complexity and your environment's complexity can co-sustain -- where each structure's persistence feeds the gradients the other depends on. The arrow of desire traces the path of ascending solvency through this space. Fortune flows not to those who occupy favorable positions but to those who actively widen the circulatory flow, deepen integration, and increase the density of viable next steps for themselves and their ecology. The luckiest agent is not the one standing where gradients converge but the one actively widening the flow.
