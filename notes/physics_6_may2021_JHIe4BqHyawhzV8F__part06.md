# Idea Flow Notes: physics_6_may2021_JHIe4BqHyawhzV8F — Experimental Procedure

## Paragraph Flow (move by move)

**Paragraph 1 — Apparatus assembly (intro line + steps 1–7)**

1. **Instruction/orientation:** "Follow the sketch of Fig.2" — points reader to the diagram so the upcoming steps don't have to be self-contained.
2. **Setup claim (anchor):** "Position the aluminium rail track on one side end of a desk." — names the first physical object and pins it to a location, handing off because every later piece attaches to this rail.
3. **Setup specification (pulley):** "Hook up the pulley on the side of the rail track that is close to the end of the desk" — adds the second component and constrains *which* end, because the next step needs that pulley as a reference point.
4. **Setup specification (photogate + measurement):** "Hook up the photogate in the rail track, 10 cm away from the pulley" — places the measurement tool a quantified distance from the pulley, so the object's run-up distance is now defined.
5. **Setup specification (test object):** "Position the aluminium object 65cm away from the photogate." — fixes the object's starting position relative to the same reference point, defining the path length.
6. **Setup connection (linkage):** "Attach the aluminium object to the string, and attach the other end of the string to the weights." — joins the two moving bodies, which is required before the string can be threaded.
7. **Setup completion (threading):** "Wrap the string around the pulley" — physically completes the force-transfer chain, handing off to a state-check.
8. **State condition:** "Suspend the weights in mid-air while the aluminium object is on the rail track" — confirms the system is pre-loaded and stationary, the precondition for the next paragraph's release.

**Paragraph 2 — Run one trial (steps 8–12)**

1. **Variable introduction (medium):** "Pour 30ml of room temperature engine oil in the beaker and then pour in in the rail track." — adds the independent-variable medium; hands off because the photogate must be live before motion starts.
2. **Measurement prep (sequencing):** "Set the photogate on before starting to take the measurements." — uses a *before* clause to lock the temporal order, so data isn't missed.
3. **Action with inline purpose:** "Release the weights to fall downward under the influence of gravity, in order to accelerate the aluminium object" — the *"in order to accelerate"* clause retroactively justifies every assembly step (pulley, string, suspended weights), handing off to measurement of the resulting motion.
4. **Data capture:** "Measure the velocity of the aluminium object while passing through the photogate." — names the dependent variable explicitly; the *"while passing through"* clause ties the reading to the instrument just switched on.
5. **Reliability directive:** "Repeat the experiment 4 times per value of temperature taken" — sets n=4, handing off to the iteration paragraph.

**Paragraph 3 — Iterate across IV values (steps 13–16)**

1. **Reset (cause→effect):** "Clean up the rail track before the next engine oil temperature is poured." — the *before* clause forces a clean state, which is the cause that lets the next pour be uncontaminated.
2. **Re-add medium:** "Pour another 30ml of engine oil in the beaker." — restocks identical volume so only temperature varies.
3. **IV step (specification):** "Increase the temperature of the engine oil by 5°C more than the previous temperature" — quantifies the increment against the *previous* value, so each step is comparable.
4. **Loop closure with endpoint:** "Repeat the steps 8-14 until the final temperature to measure is 55 °C" — names an explicit termination condition, preventing open-ended data collection.

## What This Section Does (content sequence)

1. **Apparatus assembly in spatial/anchor order** (rail first, then parts referenced to it). Sets up every distance and connection the measurement depends on.
2. **Independent-variable medium introduced at its starting value.** Sets up a clean baseline so the first reading is comparable to later ones.
3. **Instrument powered on *before* the action that triggers it.** Sets up correct temporal sequencing so no data is lost.
4. **Action released, with the physical purpose stated inline** ("in order to accelerate"). Justifies the apparatus and prepares the reader to expect a motion-based measurement.
5. **Dependent variable read at the instrument**, with the *while* clause tying reading to instrument. Sets up the data point itself.
6. **Replication directive for one IV level.** Sets up averaging and uncertainty handling.
7. **Reset + re-add + IV increment + loop endpoint.** Sets up a clean causal chain where each successive trial differs from the last in exactly one quantified way.

Why this order: you cannot measure what you haven't built; you cannot trigger what isn't powered; you cannot compare trials that differ in more than one variable; you cannot iterate without a defined stopping point.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Spatial assembly paragraph**

`SKELETON: [Reference to a diagram]. [Place anchor object at named location]. [Attach component A to anchor, specifying which end]. [Attach component B, quantified distance from component A]. [Position the moving object, quantified distance from component B]. [Connect object to driver via intermediate part]. [Thread/dress the linkage]. [State the pre-motion equilibrium].`

1. *Slots:* slot 1 = imperative referencing a figure; slots 2–7 = imperative clauses naming one new physical piece and a spatial relation (often quantified in cm); slot 8 = a *while* clause confirming the system is at rest.
2. *Fill instructions:* slot 1 = write "Follow the sketch of Fig.X"; slot 2 = pick the longest rigid piece and pin it to a desk/floor edge; slot 3 = name a force-transferring fixture (pulley, pivot, lever) and locate it at an *end* of slot 2; slot 4 = name a sensor/instrument and give its cm-distance from slot 3; slot 5 = name the object that will move and give its cm-distance from slot 4; slot 6 = use *attach… and attach…* to link moving object to driver; slot 7 = single verb for dressing/threading the link; slot 8 = use *while* to state the static pre-condition.
3. *Original fill:* "Follow the sketch of Fig.2. Position the aluminium rail track on one side end of a desk… Suspend the weights in mid-air while the aluminium object is on the rail track."
4. *Demonstration fill (different idea — pendulum period vs. bob mass):* "Follow the sketch of Fig.3. Clamp a retort stand to one corner of the bench. Fix a 1 m wooden rod horizontally across the stand's boss head, 20 cm from the clamp. Hang a 50 cm cotton string from the rod's midpoint. Tie a 20 g brass bob to the free end of the string. Loop the string once over a small screw eye. Hold the bob pulled back 10 cm from rest while the string hangs taut."

**Skeleton B — One-trial measurement paragraph**

`SKELETON: [Introduce the IV-controlled medium at its baseline value into the apparatus]. [Power on / arm the instrument *before* triggering]. [Trigger the motion, stating the physical purpose with "in order to…"]. [Read the DV *while* the object passes the instrument]. [Repeat n times per IV level].`

1. *Slots:* slot 1 = imperative adding a substance/condition; slot 2 = imperative with *before* clause; slot 3 = imperative with *under… in order to* clause; slot 4 = imperative with *while* clause; slot 5 = imperative giving an integer replication count.
2. *Fill instructions:* slot 1 = pour/spread the variable medium at its lowest or starting value; slot 2 = name the exact instrument and use *before* to force temporal order; slot 3 = name the driver (falling mass, released spring, switched-on current) and use *in order to* to state the physical effect on the object; slot 4 = name the DV explicitly and use *while* to tie reading to the instrument zone; slot 5 = write "Repeat the experiment N times per value of [IV] taken".
3. *Original fill:* "Pour 30ml of room temperature engine oil… Repeat the experiment 4 times per value of temperature taken."
4. *Demonstration fill (different idea — surface roughness vs. rolling speed):* "Spread a 50 cm strip of Grade-40 sandpaper flat along the run-up section. Switch the light gate on before releasing the cart. Release the cart down the ramp under gravity, in order to make it roll across the sandpaper. Record the cart's velocity while it interrupts the light gate. Repeat the run 5 times per surface tested."

**Skeleton C — Iteration paragraph**

`SKELETON: [Clean/reset the apparatus *before* the next IV value is applied]. [Re-introduce identical volume of medium]. [Increment the IV by a fixed amount relative to the previous value]. [Repeat the trial steps until a named final IV value].`

1. *Slots:* slot 1 = imperative with *before* clause; slot 2 = imperative identical-quantity re-add; slot 3 = imperative quantifying IV step against previous; slot 4 = imperative with *until* endpoint.
2. *Fill instructions:* slot 1 = name a residue/wear to remove and force it with *before*; slot 2 = restock the exact same mass/volume as slot 1 of Skeleton B; slot 3 = state "increase [IV] by [Δ] more than the previous [IV]"; slot 4 = write "Repeat steps X–Y until the final [IV] to measure is [terminal value]".
3. *Original fill:* "Clean up the rail track… Repeat the steps 8-14 until the final temperature to measure is 55 °C."
4. *Demonstration fill (different idea — current vs. magnetic field strength):* "Wipe the solenoid's iron core before the next coil current is set. Pour 200 mL of room-temperature water back into the calorimeter. Increase the coil current by 0.2 A more than the previous current. Repeat steps 4–9 until the final current to measure is 1.6 A."

## Express-Idea Vocabulary

- **Sequencing:** *"before starting to take the measurements"* (step 9); *"before the next engine oil temperature is poured"* (step 13).
- **Cause / consequence / purpose:** *"under the influence of gravity, in order to accelerate the aluminium object"* (step 10) — the *in order to* clause is the only purpose-marker in the section.
- **Specification (quantification):** *"10 cm away from the pulley"* (step 3); *"65cm away from the photogate"* (step 4); *"30ml of room temperature engine oil"* (step 8); *"5°C more than the previous temperature"* (step 15).
- **Endpoint / loop closure:** *"until the final temperature to measure is 55 °C"* (step 16).
- **Replication / reliability:** *"Repeat the experiment 4 times per value"* (step 12); *"Repeat the steps 8-14"* (step 16).
- **Spatial anchoring:** *"on one side end of a desk"* (step 1); *"close to the end of the desk"* (step 2) — repetition of "end" re-anchors components to the same reference point.
- **State-setting:** *"Suspend the weights in mid-air while the aluminium object is on the rail track"* (step 7) — *while* freezes the system before motion.

(Definition verbs like *defined as*, contrast markers like *however*, and authority markers like *according to* are absent from this procedural section — it relies on imperatives rather than expository verbs.)

## How to Explain an Idea (replication steps)

The section runs on a **spatial-assemble → arm → trigger-with-purpose → measure-with-while → replicate → iterate-with-endpoint** pattern. To replicate it for a new experiment:

1. **Open with a diagram reference** in one short imperative ("Follow the sketch of Fig.X") so the steps can stay terse.
2. **Build the apparatus in anchor order.** Each new component references a part already placed, and at least two distances are quantified in cm so the run is reproducible.
3. **Add the independent-variable medium at its baseline value** before any measurement instrument is switched on.
4. **Switch on / arm the measuring instrument using a *before* clause** to lock the temporal order.
5. **Trigger the motion and immediately append an *in order to* clause** stating the physical purpose — this single clause is what retroactively justifies the entire apparatus paragraph.
6. **Capture the dependent variable using a *while* clause** that ties the reading to the instrument's detection zone.
7. **State an integer replication count per IV level** ("Repeat … N times per value of [IV] taken").
8. **Reset the apparatus with a *before* clause**, re-add identical medium volume, **step the IV by a fixed increment against the *previous* value**, and **close the loop with an *until* endpoint** giving the terminal IV value numerically.

The whole explanation is carried by four small grammar devices — *before*, *in order to*, *while*, *until* — plus mandatory cm/°C/°A numbers. Strip any one and the procedure loses either reproducibility, justification, timing, or scope.
