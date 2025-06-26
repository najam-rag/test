
import streamlit as st

st.title("Electrical Questionnaire")

st.markdown("""Q: What are the fundamental principles established by AS/NZS 3000 for providing protection against dangers and damage?
A: Clause 1.5.1 of AS/NZS 3000 outlines protection principles to safeguard people, livestock, and property against risks arising from electrical installations. It identifies three major types of risk:
   (a) Shock current — from direct or indirect contact with live parts.
   (b) Excessive temperatures — that may cause burns, fires, or material degradation.
   (c) Explosive atmospheres — where equipment must prevent ignition of flammable gases or dust.
Q: What is the definition of direct contact according to Clause 1.4.38 of AS/NZS 3000?
A: Clause 1.4.38 of AS/NZS 3000 defines *direct contact* as a situation where a person comes into contact with a conductor or conductive part that is live under normal service conditions. In other words, it refers to exposure to electrical parts that are intentionally energized during the usual operation of an electrical installation.
Q: According to Clause 1.5.4.1 of AS/NZS 3000, how is protection against direct contact generally achieved?
A: Clause 1.5.4.1 of AS/NZS 3000 explains that protection against direct contact can be provided through several methods. These methods are all designed to safeguard individuals from dangers that may result from touching parts of an electrical installation that are live during normal service. The goal is to eliminate or reduce the risk of electric shock by preventing unintended access to live conductive components.
Q: What methods does Clause 1.5.4.2 of AS/NZS 3000 specify for protecting against direct contact with live parts?
A: Clause 1.5.4.2 of AS/NZS 3000 outlines four primary methods that can be used individually or in combination to prevent direct contact with live electrical parts. These methods are:
1. **Insulation** – Ensuring that live parts are covered with insulating material to prevent accidental contact.
2. **Barriers** – Using physical covers or enclosures to restrict access to live components.
3. **Obstacles** – Positioning items in such a way that access to live parts is obstructed, reducing the likelihood of accidental contact.
4. **Placing Out of Reach** – Installing live parts at a height or location that is not easily accessible without assistance.
These approaches aim to reduce the risk of electric shock during normal operation of electrical installations.
Q: What does Clause 1.5.4.3 of AS/NZS 3000 state about protection by insulation, and do paint, enamel, or varnishes qualify as adequate insulation?
A: Clause 1.5.4.3 of AS/NZS 3000 states that live parts must be completely covered with insulation that is capable of withstanding the mechanical, chemical, electrical, and thermal conditions expected during service. This insulation must be durable and effective in preventing direct contact.
Importantly, materials such as paint, enamel, or varnish **do not** provide adequate protection against direct contact. These coatings are not considered reliable insulating materials under the Standard, and therefore cannot be used to meet the insulation requirement.
Q: According to Clause 1.5.4.4 of AS/NZS 3000, how should protection by barriers or enclosures be implemented to safeguard against direct contact?
A: Clause 1.5.4.4 of AS/NZS 3000 specifies that when live parts are protected by barriers or enclosures, the degree of protection must meet the following minimum standards:
1. **IP2X** – for general protection against contact with fingers or similar objects.
2. **IP4X** – specifically required for horizontal surfaces to prevent ingress of small objects.
Additionally, access to live parts by removing doors, lids, or covers must not be possible unless:
- A **key or tool** is required to open the barrier,
- An **interlocking device** ensures safety before access, or
- There is an **intermediate barrier** that maintains protection even if the outer cover is removed.
These requirements ensure that live parts are not easily exposed, thereby preventing accidental contact and improving safety during maintenance or inspection.
Q: What does Clause 1.5.4.5 of AS/NZS 3000 state about protection by obstacles?
A: Clause 1.5.4.5 of AS/NZS 3000 explains that protection by **obstacles** is designed to prevent **unintentional contact** with live parts. These obstacles are not intended to stop **intentional contact**, where a person might deliberately bypass or circumvent the protection.
This method is typically used in controlled environments, such as restricted-access areas or where only skilled persons are permitted, and relies on the awareness and behavior of those present to maintain safety.
Q: According to Clause 1.5.4.6 of AS/NZS 3000, what does protection by placing out of reach involve?
A: Clause 1.5.4.6 of AS/NZS 3000 describes that protection by **placing out of reach** involves installing live parts in such a way that they are not accessible during normal conditions — specifically **beyond arm's reach**.
It further clarifies that **simultaneously accessible parts at different voltages** must not be within **2.5 metres** of each other. This ensures that a person cannot accidentally touch two different voltage sources at the same time, reducing the risk of electric shock or current flow through the body.
Q: How is "arm’s reach" defined according to Clause 1.4.12 of AS/NZS 3000?
A: Clause 1.4.12 of AS/NZS 3000 defines **arm’s reach** as the distance a person can **reach without assistance**, measured from any point on a surface where people typically **stand** or **move about**. 
This concept is used in the Standard to determine safe distances for the placement of live parts and equipment to prevent unintentional contact.
Q: What are the defined limits of arm’s reach in different directions according to AS/NZS 3000?
A: AS/NZS 3000 specifies the following limits for **arm’s reach** from a surface where a person can stand or move about:
- **Above the surface**: 2.5 metres  
- **Adjacent to the surface (sideways)**: 2.5 metres  
- **Below the surface**: 1.25 metres
These dimensions help determine safe zones for the placement of live electrical parts and ensure they are installed out of unintentional reach to prevent electrical hazards.
Q: What does Clause 1.5.5.1 of AS/NZS 3000 state about protection against indirect contact?
A: Clause 1.5.5.1 of AS/NZS 3000 requires that protection must be provided against **dangers** that may result from contact with **exposed conductive parts** which could become live **under fault conditions**. 
This type of risk, known as **indirect contact**, occurs when normally non-live metal parts of electrical equipment become energized due to insulation failure or other faults. Protective measures such as earthing, circuit breakers, or RCDs are necessary to minimize this hazard and ensure safety.
Q: How is "indirect contact" defined according to Clause 1.4.35 of AS/NZS 3000?
A: Clause 1.4.35 of AS/NZS 3000 defines **indirect contact** as contact with a **conductive part** that is **normally accessible** and becomes **live only under fault conditions**.
These conductive parts are not meant to carry current during normal operation, but if a fault occurs (such as insulation failure), they may pose a risk of electric shock — which is why protective measures like earthing and automatic disconnection are essential.
Q: What is the definition of indirect contact according to Clause 1.4.35 of AS/NZS 3000?
A: Clause 1.4.35 of AS/NZS 3000 defines **indirect contact** as contact with a **conductive part** that is **normally accessible** and becomes **live only under fault conditions**. 
This typically includes metal enclosures or frames of electrical equipment that are not intended to carry current during normal operation but could become energized due to insulation failure or other faults. Proper earthing and fault protection are required to manage this risk.
Q: According to Clause 1.5.5.2 of AS/NZS 3000, what are the methods used to protect against indirect contact?
A: Clause 1.5.5.2 of AS/NZS 3000 outlines four primary methods for providing protection against **indirect contact** — that is, contact with conductive parts that may become live under fault conditions. These methods include:
1. **Automatic Disconnection of Supply** – Using protective devices like circuit breakers or RCDs to quickly disconnect power in the event of a fault.
2. **Use of Class II Equipment** – Employing equipment with double or reinforced insulation, which doesn’t rely on protective earthing.
3. **Electrical Separation (as per Clause 5.5.5)** – Isolating the electrical circuit from other circuits and earth to prevent fault current flow.
4. **Limitation of Fault Current** – Designing the installation in a way that limits the amount of fault current to non-hazardous levels.
These approaches are intended to minimize the risk of electric shock and ensure compliance with safety requirements.
Q: What is the most commonly used method to protect against indirect contact according to AS/NZS 3000?
A: The most commonly used method to protect against **indirect contact** is **automatic disconnection of supply**.
This method involves the use of protective devices such as **circuit breakers** or **residual current devices (RCDs)** that detect fault conditions — like current flowing through an unintended path — and **quickly disconnect power**. This rapid action helps prevent electric shock or further damage when conductive parts become live due to a fault.
Q: How are electrical equipment classes (Class I, II, III) defined in AS/NZS 3000, and how do they protect against electric shock?
A: AS/NZS 3000 classifies electrical equipment into **Class I, Class II, and Class III**, based on the method of protection against electric shock:
🔹 **Class I Equipment** (Clause 1.4.27):  
Protection is provided through **basic insulation** between live parts and exposed conductive parts. These conductive parts are connected to **protective earthing**, so that if the insulation fails, the circuit’s protective device (like a fuse or breaker) disconnects the supply.  
*Examples*: A metal light switch or a washing machine with a metal body.
🔹 **Class II Equipment** (Clause 1.4.28):  
Provides protection through **double insulation** or **reinforced insulation** between live parts and accessible surfaces. These devices **do not require protective earthing**. Such equipment is marked with the **Class II symbol (a square inside a square)**.  
*Examples*: Power tools with plastic housing or insulated phone chargers.
🔹 **Class III Equipment** (Clause 1.4.29):  
Protection is based on the use of **Separated Extra-Low Voltage (SELV)** — not exceeding **50V** at no load. The voltage is supplied by an isolating transformer or similar means to ensure it cannot exceed safe levels.  
*Reference: Clause 1.4.83 defines SELV as a voltage isolated from mains by a safety transformer or converter with separate windings.*
This classification helps ensure electrical equipment is used safely according to the level of risk in its environment.
Q: What is "touch voltage" according to Clause 1.4.95 of AS/NZS 3000?
A: Clause 1.4.95 of AS/NZS 3000 defines **touch voltage** as the **voltage between simultaneously accessible parts** that a person could come into contact with at the same time.
This voltage becomes a safety concern when there is a fault, such as an insulation failure or grounding issue, that allows a difference in potential between exposed conductive parts or between an exposed part and earth — creating the risk of electric shock. Ensuring touch voltages remain within safe limits is a core goal of protective earthing and bonding systems.
.Q: What is "touch current" according to Clause 1.4.94 of AS/NZS 3000?
A: Clause 1.4.94 of AS/NZS 3000 defines **touch current** as the **current that flows between simultaneously accessible parts** when a person comes into contact with them.
This current may pass through the human body if those parts are at different electrical potentials — posing a risk of electric shock. Managing touch current is critical for safety, and standards ensure it remains below hazardous levels through proper insulation, earthing, and protective devices.
Q: According to Clause 1.5.8 of AS/NZS 3000, how must electrical installations be arranged to protect against thermal effects in normal service?
A: Clause 1.5.8 of AS/NZS 3000 states that electrical installations must be arranged so that there is **no risk of ignition of flammable materials** due to:
- **High temperature**, or  
- **Arcing (ARC)**  
during **normal operation** of the electrical system.
This requirement ensures that heat or electrical discharges generated during routine use do not pose a fire hazard, especially in environments where combustible materials are present. Proper equipment selection, clearances, and thermal insulation play a key role in meeting this safety standard.
Q: According to Clause 1.5.12 of AS/NZS 3000, what must be maintained when a wiring system passes through a wall, floor, or ceiling?
A: Clause 1.5.12 of AS/NZS 3000 requires that when a **wiring system passes through a wall, floor, or ceiling**, the **fire rating of that building element must be maintained**.
This means that any penetration by electrical cables must not compromise the structure’s ability to contain or resist the spread of fire. To comply, installers must use approved fire-rated materials, sealants, or fire collars that restore the original fire-resistance level of the wall or barrier. This is a critical fire safety measure in both residential and commercial installations.
 Q: According to Clause 1.5.9 of AS/NZS 3000, how is protection against overcurrent achieved?
A: Clause 1.5.9 of AS/NZS 3000 outlines two key methods for providing **protection against overcurrent**, which refers to currents exceeding the safe operating limits of conductors or equipment. These methods are:
1. **Automatic Disconnection of Supply** – Devices like fuses and circuit breakers detect overcurrent conditions and automatically interrupt the supply to prevent damage, overheating, or fire.
2. **Limiting the Maximum Overcurrent and Its Duration** – By designing systems that restrict how high the overcurrent can rise and how long it can persist, the risk of damage is minimized even if automatic disconnection is not immediate.
These measures are essential to ensure the integrity and safety of electrical installations.
Q: What is an overcurrent, and what are common causes of overcurrent in an electrical circuit?
A: An **overcurrent** is a condition where the current **exceeds a particular rated value** for a conductor or device, potentially leading to overheating, equipment damage, or fire.
Common causes of overcurrent include:
1. **Short Circuit** – A direct connection between conductors of different potentials causing a sudden surge of current.
2. **Excessive Load** – Drawing more current than the circuit is designed to carry, such as connecting too many devices.
3. **Incorrect Design** – Poorly sized cables or protective devices that fail to match the circuit's actual demand or application.
Proper circuit design and protective measures are essential to detect and interrupt overcurrents before they become hazardous.
Q: According to Clause 1.4.37 of AS/NZS 3000, what is a fault current?
A: Clause 1.4.37 defines a **fault current** as a **current resulting from either an insulation failure or from the bridging of insulation**.
This type of current flows through unintended paths in the electrical system, such as between a live conductor and earth or another conductor. Fault currents are dangerous because they can lead to electric shock, equipment damage, or fire. Detecting and interrupting fault currents promptly is a key function of protective devices like fuses and circuit breakers.
Q: According to Clause 1.4.38 of AS/NZS 3000, what is an overload current?
A: Clause 1.4.38 defines an **overload current** as a **current that flows in a circuit which is electrically sound**, but the current exceeds the normal full-load rating of the circuit components.
Unlike fault currents, overload currents do not result from insulation failure or short circuits. Instead, they arise when the connected load draws more current than the circuit is designed to handle — for example, when too many appliances are plugged into a single circuit. If sustained, overload currents can cause overheating and damage, which is why protective devices are used to disconnect the supply under such conditions.
Q: According to Clause 1.4.39 of AS/NZS 3000, what is a short-circuit current?
A: Clause 1.4.39 defines a **short-circuit current** as a **fault current that arises from the bridging of insulation**, typically resulting in a direct connection **between live conductors or between a live conductor and earth**.
This unintended connection allows a large current to flow through an abnormal path with very low resistance, which can cause rapid heating, arcing, or even fire. Short-circuit protection — such as circuit breakers and fuses — is critical to interrupt this current quickly and prevent damage or injury.
Q: According to Clause 1.5.10 of AS/NZS 3000, what requirement must protective earthing conductors meet regarding earth fault currents?
A: Clause 1.5.10 of AS/NZS 3000 specifies that **protective earthing conductors** and any other components intended to carry **earth fault currents** must be capable of doing so **without reaching excessive temperature**.
This requirement ensures that during a fault condition, the conductors can safely carry high currents for the required disconnection time without degrading insulation, damaging nearby materials, or posing a risk to people or equipment. Proper conductor sizing and compliance with thermal limits are essential to meeting this standard.
Q: According to Clause 2.7.1 of AS/NZS 3000, what are common causes of overvoltage in an electrical installation?
A: Clause 2.7.1 explains that **overvoltage** can occur in an electrical installation due to several factors that can raise the voltage above the system's normal operating level. These causes include:
1. **Insulation fault between different voltage circuits** – leading to unintended voltage transfer.
2. **Switching operations** – such as sudden disconnection or reconnection of loads, especially inductive ones.
3. **Lightning** – direct strikes or nearby atmospheric discharges inducing high voltage transients.
4. **Resonant phenomena** – specific circuit conditions amplifying voltage levels.
These scenarios can damage sensitive equipment or create safety hazards, which is why surge protection devices (SPDs) and proper system design are vital.
Q: How can protection against overvoltage be achieved according to AS/NZS 3000?
A: Protection against **overvoltage** in electrical installations can be achieved through two primary methods:
1. **Protection by Insulation or Separation** – Ensuring sufficient insulation strength or physical separation between components to withstand transient or sustained overvoltage conditions.
2. **Protective Devices** – Installing devices such as **Surge Protection Devices (SPDs)**, voltage limiters, or circuit breakers designed to detect and suppress overvoltage events, including those caused by lightning or switching surges.
Together, these measures help safeguard both the electrical system and connected equipment from potential damage due to abnormal voltage conditions.
Q: What is a common method used to protect circuits and equipment from the effects of overvoltage?
A: A widely used and effective method to protect electrical **circuits and equipment** from the harmful effects of **overvoltage** is the installation of a **Surge Protection Device (SPD)**.
SPDs are designed to limit transient overvoltages by diverting excess voltage safely to earth. These devices protect sensitive components from voltage spikes caused by lightning, switching operations, or faults in nearby systems. They are essential in both residential and commercial installations where voltage surges could lead to costly equipment damage or safety hazards.
Q: According to Clause 1.5.13 of AS/NZS 3000, when must protection be provided against injury from mechanical movement?
A: Clause 1.5.13 of AS/NZS 3000 states that **protection must be provided** where the **mechanical movement of electrically actuated equipment** poses a risk of injury. This includes situations where:
1. The **movement involves a risk of physical injury**, such as entrapment, crushing, or impact.
2. **Emergency stopping** may be necessary to quickly eliminate unexpected danger caused by equipment motion.
This requirement ensures that safeguards—such as interlocks, guards, or emergency stop mechanisms—are in place to protect people from moving parts during both normal operation and fault conditions.
Q: What safety requirement must be met when installing electric motors according to AS/NZS 3000?
A: According to AS/NZS 3000, **electric motors must be provided with suitable devices** that allow for the **disconnection or isolation** of electrical equipment.
This ensures that maintenance, inspection, or emergency shutdowns can be performed **safely**, without exposing personnel to live parts or unintended motor operation. These devices may include **manual isolators, circuit breakers with disconnection features, or motor isolators** installed in accessible locations.
Q: What requirement must be met for electric motors under AS/NZS 3000?
A: AS/NZS 3000 specifies that **electric motors must be provided with suitable devices** to **disconnect or isolate** the electrical equipment.
This ensures that during servicing, maintenance, or in case of emergency, the motor can be safely de-energized to prevent electrical shock or mechanical hazards. Isolation devices must be **readily accessible**, clearly identified, and capable of securely interrupting the power supply to the motor.
Q: What is the nominal voltage and frequency for electrical supply in Australia?
A: The **nominal supply voltage** in Australia is **230 V** for single-phase systems and **400 V** for three-phase systems. The supply is **generated at a frequency of 50 Hz**.
This standard aligns with the International Electrotechnical Commission (IEC) recommendations and ensures compatibility of appliances, installations, and equipment across Australian networks.
Q: How is the number of supply phases determined in an electrical installation under AS/NZS 3000?
A: According to AS/NZS 3000, the **number of supply phases** connected to an installation depends on both the **maximum demand** and the **type of electrical load**. The general guidelines are:
- For **installations with a maximum demand less than 100 A**, a **single-phase (1Ph)** supply is typically permitted.
- For **installations exceeding 100 A**, or those that contain **three-phase equipment**, a **three-phase (3Ph)** supply is generally required.
This ensures adequate capacity and balanced load distribution, especially in commercial or industrial environments.
Q: What are the permitted methods for determining maximum demand according to Clause 2.2.2 of AS/NZS 3000?
A: Clause 2.2.2 of AS/NZS 3000 outlines **four permitted methods** that can be used to determine the **maximum demand** of an electrical installation:
1. **Calculation** – Applying standard demand factors and diversity rules as outlined in the Standard.
2. **Measurement** – Using actual load measurements taken from similar or existing installations.
3. **Assessment** – Using engineering judgment based on known data and usage patterns.
4. **Limitation** – Restricting load by design, such as installing circuit limiters or setting contract limits.
These methods ensure the installation is adequately designed to handle expected loads safely and efficiently.
Q: What does "Maximum Demand by Calculation" mean under AS/NZS 3000?
A: **Maximum Demand by Calculation** refers to determining the expected electrical load by summing the **actual power ratings** of all connected equipment, **without applying diversity factors**.
This approach uses real load data (in watts or amps) to estimate the highest possible load an installation might draw. It is often used for **small installations**, preliminary design, or when precise data is available.
📌 **Example**:
If an installation has:
- 1 × oven: 2.4 kW  
- 1 × water heater: 3.6 kW  
- 10 × lights @ 60W each: 0.6 kW  
**Total calculated demand** = 2.4 + 3.6 + 0.6 = **6.6 kW**
This value can then be used to size conductors, circuit protection, and supply arrangements.
Q: "What does 'Maximum Demand by Calculation' mean in electrical design under AS/NZS 3000?",
A: "Maximum Demand by Calculation means determining the total electrical load without applying diversity factors, based purely on known equipment ratings. Here's an example for a small household:
**Scenario**: Small Household
1. General Power Outlets (GPOs): 10 outlets × 100 W = 1000 W → Current = 1000 / 230 ≈ 4.35 A  
2. Lighting: 8 × 15 W = 120 W → Current = 120 / 230 ≈ 0.52 A  
3. Cooking Appliances: Oven (4.5 kW) + Cooktop (2.5 kW) = 7000 W → Current = 7000 / 230 ≈ 30.43 A  
4. Hot Water System: 3.6 kW → Current = 3600 / 230 ≈ 15.65 A  
5. Air Conditioning: 3.5 kW → Current = 3500 / 230 ≈ 15.22 A
**Total Maximum Demand (Amps)**:  
= 4.35 + 0.52 + 30.43 + 15.65 + 15.22  
= **66.17 A**
**Convert to Power**:  
= 66.17 × 230 / 1000 ≈ **15.22 kW**
📌 **Result**: The maximum demand for this installation is **66.17 A** or **15.22 kW**, using the pure calculation method without diversity."
Q: "How is Maximum Demand calculated using the 'Assessment Method' with diversity under AS/NZS 3000?",
A: "Maximum Demand by Assessment includes applying diversity factors to account for the probability that not all connected loads operate simultaneously at full capacity. It provides a more realistic demand estimation.
🔢 **Formula**:  
Diversity = Maximum Demand / Total Connected Load
🧮 **General Diversity Factors** (Rule of Thumb):  
- Lighting: 1  
- Kitchenette equipment: 0.8  
- Cleaner’s equipment: 0.1  
- General Purpose Outlets (GPOs): 0.5  
- Mechanical Units: 0.8  
- Hot Water System: 0.8  
📘 **Scenario**: Small Household Example
1. **General Power Outlets (GPOs)**  
- Load: 10 × 100 W = 1000 W  
- Current = 1000 / 230 = 4.35 A  
- Apply diversity: 4.35 × 0.5 = **2.17 A**
2. **Lighting**  
- Load: 8 × 15 W = 120 W  
- Current = 120 / 230 = **0.52 A** (No diversity applied)
3. **Cooking Appliance**  
- Load: Oven + Cooktop = 7000 W  
- Current = 7000 / 230 ≈ 30.43 A  
- Apply diversity: 30.43 × 0.8 = **24.3 A**
4. **Hot Water System**  
- Load: 3600 W  
- Current = 3600 / 230 ≈ 15.65 A  
- Apply diversity: 15.65 × 0.8 = **12.52 A**
5. **Air Conditioning**  
- Load: 3500 W  
- Current = 3500 / 230 ≈ 15.22 A  
- Apply diversity: 15.22 × 0.8 = **12.17 A**
📊 **Combined Maximum Demand**  
Total current = 2.17 + 0.52 + 24.3 + 12.52 + 12.17 = **51.68 A**
🔌 **Converted to Power**  
= 51.68 × 230 / 1000 ≈ **11.2 kW**
✅ **Final Result**:  
Maximum Demand using assessment = **51.68 A** or **11.2 kW**, incorporating realistic diversity for household usage."
Q: What does "Maximum Demand by Assessment" mean under AS/NZS 3000 and how is it calculated for a small household?
A: **Maximum Demand by Assessment** under **AS/NZS 3000** involves using Tables C1, C2, and C3 to estimate demand based on standard assumptions. Here's a sample scenario:
**Scenario – Small Household:**
1. **GPOs (10 outlets):** Table C1 → 10 A  
2. **Lighting (8 points):** Table C1 → 10 A  
3. **Cooking Appliances (7 kW total):** Table C1 → 13 A  
4. **Hot Water System (3.6 kW):** Assessed at full load → 15.65 A  
5. **Air Conditioning (3.5 kW):** Assessed at full load → 15.22 A  
**Step-by-Step:**
- **Diverse Loads (GPOs + Lighting + Cooking):**  
  Sum = 10 + 10 + 13 = 33 A  
  Apply diversity factor of 0.75 → 33 × 0.75 = **24.75 A**
- **Non-Diverse Loads:**  
  Hot water + A/C = 15.65 + 15.22 = **30.87 A**
- **Total Maximum Demand:**  
  24.75 + 30.87 = **55.62 A**
- **Convert to kW:**  
  55.62 × 230 / 1000 ≈ **12.79 kW**
**Result:** Maximum Demand = **55.62 A** or **12.79 kW**, calculated entirely by assessment per AS/NZS 3000:2018.
Q: What does "Maximum Demand by Measurement" mean under AS/NZS 3000?
A: **Maximum Demand by Measurement** refers to determining the maximum electrical load based on actual usage data collected over time.  
**Measurement Tools:**  
1. Power meters or energy analyzers (digital or analog)  
2. Smart meters installed by electricity utilities  
3. Data loggers for tracking load patterns  
**Monitoring Period:**  
- Typically spans a billing cycle (e.g., 30 days)  
- Utilities often assess 15-minute or 30-minute intervals  
- Maximum average demand during these intervals is used to determine demand  
Q: What does "Maximum Demand by Limitation" mean under AS/NZS 3000?
A: **Maximum Demand by Limitation** refers to the practice of capping or artificially restricting the maximum electrical load that can be drawn by an installation. This ensures the system stays within safe operational limits or cost-efficient thresholds.
**Purpose:**  
- To ensure the electrical load does not exceed the capacity of supply components (e.g., transformers, cables, or circuit breakers).  
- To reduce utility demand charges based on peak electricity usage.
**Implementation Methods:**  
- **Load-Shedding Systems:** Automatically disconnect non-critical loads when demand nears the maximum threshold.
**Example – Residential Setting:**  
- **Supply Capacity:** 63 A  
- **Calculated Demand:** 80 A  
- **Solution:** Install a demand controller that monitors total load. Non-essential equipment like pool pumps or EV chargers is disconnected automatically when the load approaches 63 A.
Q: What does AS/NZS 3000 Clause 3.6.2 say about voltage drop?
A: **Clause 3.6.2** of AS/NZS 3000 specifies that the voltage drop between the point of supply and any point within the low voltage electrical installation must **not exceed 5%** of the nominal voltage at the point of supply. This requirement ensures that equipment receives sufficient voltage for safe and efficient operation, minimizing risks of malfunction, overheating, or energy loss.
Q: What is the purpose of arranging electrical installations into circuits according to Clause 1.6.5 of AS/NZS 3000?
A: **Clause 1.6.5** of AS/NZS 3000 emphasizes that electrical installations should be arranged into circuits to **minimize inconvenience** in the event of a fault. This arrangement also helps to:
1. Avoid danger,
2. Minimize inconvenience,
3. Facilitate safe operation, testing, and maintenance.
Q: As per Clause 1.4.3 of AS/NZS 3000, what is meant by the term “readily accessible”?
A: **Clause 1.4.3** defines **"readily accessible"** as something that can be reached without the use of tools, ladders, or other aids and is **not more than 2.0 meters** above the floor or ground level.
Q: As per Clause 1.4.16 of AS/NZS 3000, what is meant by the term “arm's reach” and what are the limits of arm's reach?
A: **Clause 1.4.16** defines **"arm's reach"** as the distance a person can extend their hand in any direction **without assistance**, from a surface where people usually **stand or move about**.  
The standard limits of arm's reach are:
- **Above or adjacent to a surface**: 2.5 meters  
- **Below a surface**: 1.25 meters
As per Clause 1.4.31, what level of insulation applies to Class I equipment?
Single level insulation between live parts and exposed conductive parts, with earthing for fault protection.
Q: As per Clause 1.4.38, what is direct contact?
A: Contact with a part that is live under normal service.
Q: As per Clause 1.4.39, a person receives an electric shock from the metal frame of an electric motor. A: According to AS/NZS 3000:2007, what is the name given to this type of contact?
Indirect contact.
Q: As per Clause 1.4.39, a circuit does not have an electrical fault but draws excessive current. What is the name given to this current?
A: Overload current.
Q: As per Clause 1.4.87, what is the definition of an obstacle?
A: A physical barrier intended to prevent unintentional contact with live parts.
Q: As per Clause 1.4.125, describe the meaning of the term “touch voltage”.
A: The voltage present between simultaneously accessible parts during a fault.
Q: As per Clause 1.4.124, what is meant by the term “touch current”?
A: The electric current that flows between simultaneously accessible conductive parts.
Q: As per Clause 1.5.1, list the three major types of risk in an electrical installation as identified by AS/NZS 3000:2007. A Shock current, Excessive temperature, Explosive atmospheres
Q: As per clause 1.4.124, if a “touch voltage” exceeds certain values, a protective device must disconnect the supply. What are the limits of “touch voltage”?
A: Touch voltage must not exceed 50V AC or 120V DC. If exceeded, automatic disconnection is required.
Q: When protection against indirect contact is provided by automatic disconnection of the supply, what is the maximum disconnection time for each of the following?
A:
(a) Power circuit < 63A: 0.4 seconds
(b) Equipment with only single insulation: 0.4 seconds
(c) Electric range: 5 seconds
(d) Submain: 5 seconds
(Reference: AS/NZS 3000 Clause 5.7.2)
Q: What does Clause 1.6 of AS/NZS 3000 say about the arrangement into circuits?
A: To meet design and safety requirements, installations must be split into circuits. These include:
• Consumer Mains – connect the entire installation to the street supply at one point for isolation.
• Submains – connect between switchboards, with no direct load connected.
• Final Subcircuits – connect loads to the main switchboard or sub-distribution board.
Q: According to Clause 1.6.5 of AS/NZS 3000, why should electrical installations be divided into circuits?
A: Installations must be divided into circuits to:
• Avoid danger and minimize inconvenience during faults.
• Facilitate safe operation, inspection, testing, and maintenance.
Q: What additional considerations are important when designing and separating circuits?
A: Logical grouping of circuits by function or area, Safety services (e.g., emergency lighting) on separate dedicated circuits.
Q: What are six typical load groups that are divided into separate final sub-circuits?
A:
Lighting
Socket outlets
HVAC (Heating, Ventilation & Air Conditioning)
Motor-driven plant
Auxiliary services
Safety services
Q: Based on Appendix C (Table C8) of AS/NZS 3000, how should a domestic home with specific loads be arranged into circuits?
A: Example circuit arrangement:
Q:  Commercial Office is wired using T.P.S. cable and has the following load 
items installed: 
 43 lights (20A C.B.) 
 23 10A Socket Outlets (20A C.B.) 
Complete the following table:
Q: What is a SELV circuit?
A: A SELV (Separated Extra-Low Voltage) circuit is a safety system designed to operate at low voltages to prevent electric shock. It is typically used in Zone 0 (such as inside bathtubs or shower bases), where no earth return is required.
SELV circuits are powered by a safety isolating transformer or a separated winding power supply, ensuring the output is electrically separated from earth and other circuits for maximum safety.
Q: What is a PELV circuit?
A: A PELV (Protected Extra-Low Voltage) circuit is a type of extra-low voltage system used in applications where low voltage is required and the risk of electric shock is relatively low. Unlike SELV, PELV systems may have a connection to earth—meaning exposed conductive parts of the equipment can be earthed for safety.
PELV is commonly used outside hazardous areas and in general control systems, offering protection through basic insulation and earth bonding rather than total electrical separation.
Q: Voltage drop at any point in an extra-low voltage electrical installation shall not exceed ?
A: Voltage drop at any point in an extra-low voltage electrical installation shall not exceed 10% of the nominal value at IB (design current of the final subcircuit) unless the equipment is specifically designed for such operation.
Q: What is an isolated supply as per AS/NZS 3000?
A: An isolated supply refers to a power source that operates independently of the utility grid, with no direct connection to the main distribution network. It typically consists of standalone power sources such as:
Diesel or gas-powered generators
Solar PV systems with battery storage
UPS (Uninterruptible Power Supply) systems in standalone mode
The supply is electrically isolated to avoid unintentional grid connection, ensuring safety and compliance.
Purpose of isolated supply:
Prevents backfeeding into the utility network (protecting maintenance personnel)
Enables reliable supply in remote or off-grid areas
Provides continuity of service in critical facilities (e.g., hospitals, data centers) during grid outages
Examples:
Off-grid solar homes
Backup generator setups with grid isolation
Temporary power sources at construction sites or events
Q: What is an isolated supply as per AS/NZS 3000?
A: An isolated supply refers to a power source that is:
Independent of the utility grid: It has no direct electrical connection to the main electricity network.
Standalone power source such as:
Diesel or gas generators
Solar PV systems with batteries and inverters
UPS systems in standalone/off-grid mode
Electrically isolated: Designed to prevent unintentional connection to other power sources or the grid.
Purpose of Isolated Supply:
✅ Safety: Prevents backfeeding into the grid (protects utility workers)
✅ Reliability: Powers remote/off-grid areas
✅ Continuity: Ensures critical loads (e.g. hospitals, data centers) stay operational during outages
Examples:
🏠 Off-grid homes using solar+batteries
🏥 Backup generators in hospitals
🏗️ Portable generators at construction sites or events
(Reference: AS/NZS 3000:2018 – Definitions and Clause context)
Q: Refer to Clause 7.4.3 – Arrangement of circuits. What are the requirements for separated circuits under AS/NZS 3000?
A: Separated circuits shall comply with the following:
(a) Circuit voltage shall not exceed 500 V.
(b) All live parts of a separated circuit shall be reliably and effectively electrically separated from all other circuits, including other separated circuits and earth.
(c) Exposed conductive parts of electrical equipment supplied by a separated circuit shall not be connected to the protective earthing conductor, or to the exposed conductive parts of the source of supply.
(d) Cables and supply flexible cords to the equipment shall be protected against mechanical damage or arranged so that any damage is readily visible.
(Reference: AS/NZS 3000 Clause 7.4.3)
Q: List 3 precautions which may be used to prevent electrical equipment from being inadvertently (accidentally) energized.
A:
Provision of a padlock on isolating switches or circuit breakers.
Use of warning tags to indicate that the equipment is under maintenance or inspection.
Placing the equipment within a lockable space to restrict unauthorized access.
Q: Refer to Clause 2.3.3.3 – Location
In general, where shall main switches be located?
A:
Readily accessible, and located
Not more than 2m above finished floor level (AFFL)
In multiple installations (e.g., flats or living units), each occupier shall have a separate isolator
Q: Read clauses 7.2.1.2 and 7.2.1.3 and list 6 types of safety service that would be separate from one another and controlled by their own main switch.
A:
Escalators
Lift in a single private residence
Lifts not defined as emergency lifts
Jacking pumps
Fire Detection and Control Indicating Equipment (FDCIE)
Smoke alarms in a single private residence
Q: A circuit for a fixed or stationary cooking appliance having an open cooking surface incorporating electric heating elements (e.g., cooktops, deep fat fryers, barbecue griddles) must meet what switching requirements?
A: The circuit must be provided with a switch operating in all active conductors, mounted near the appliance in a visible and readily accessible position.
Q: Is there any exception to the above requirement?
A: Yes. An exception exists for cooktops installed in public parks.
Q: What is the required mounting distance for a functional switch controlling a cooktop?
A: The functional switch should be mounted within 2 metres of the appliance.
Q: Does a built-in wall oven require a functional switch?
A: No.
Q: Does an upright stove require a functional switch?
A: Yes.
Q: What recommendation is provided for the installation of functional switches to control domestic appliances?
A:
The switch shall not be mounted on the cooking appliance.
It should be mounted within 2 metres of the appliance.
The switch must not be located such that the user has to reach across the open cooking surface to operate it.
Q: Which of the following considerations is not necessary in determining the number and type of circuits within an electrical installation?
A: Seasonal and daily variations of demand
Q: When selecting a circuit breaker for a water heater final sub-circuit, its current rating should be:
A: equal to or greater than the demand of the final sub-circuit and equal to or less than the cable rating
Q: A separate final sub-circuit is recommended for any single point of load exceeding:
A: 20A
Q: The recommended number of lighting points that can be connected to a circuit wired in 1.0 mm² TPS cable and protected by a 6A type C circuit breaker in a domestic installation is:
A: 10 (Refer Table C9 of AS/NZS 3000)
Q: The recommended number of double 10A socket outlets that can be connected to a circuit wired in 2.5 mm² TPS cable and protected by a 20A type C circuit breaker in a factory without air conditioning is:
A: 10 (Refer Table C8 of AS/NZS 3000
Q: The switch used to isolate a 12.5 kW range (cooktop and oven) that is connected to two phases and neutral, would have as a minimum:
A: three poles
Q: For a single domestic installation, with a maximum demand of less than 100 A, the maximum number of main switches per tariff is
A: 1
Q: A main switch should be located;
A: at the main switch board
Q: The maximum permissible height for a main switch above the ground, a floor or platform is;
A: 2.0m
Q: Is it permitted to install an isolation switch in a neutral conductor?
A: Yes, but only if all active conductors are also isolated simultaneously (e.g., via a multipole switch). Isolating the neutral alone is not permitted.
Q: Is it permitted to install an isolation switch in a protective earthing conductor?
A: No, it is not permitted. Protective earthing conductors must remain permanently connected to ensure continuous safety and fault protection.
Q: A house contains :  22 x lighting points protected by a 10 A C.B  16 x double 10 A S/O’s protected by a 20 A C.B.  1 x 15 A S/O for a clothes drier protected by a 20 C.B.  1 x 13 A A/C unit protected by a 20 C.B  1 x 800 W heat pump HWS. protected by a 20 C.B
Q: AS/NZS 3000 defines a SELV wiring system as:
A: Electrically separated from earth and from other systems. (Clause 1.4.105)
Q: AS/NZS 3000 defines a PELV wiring system as:
A: Not electrically separated from earth but satisfies all other requirements of SELV. (Clause 1.4.96)
Q: The nominal voltage of a SELV or PELV wiring system shall not be capable of exceeding?
A: 50V AC or 120V DC
Q: Can an Extra Low Voltage cable be run in a common conduit with a cable supplied at Low Voltage?
A: Yes, if a minimum distance of 50 mm is maintained or double insulation wiring is used. However, it's preferable to avoid it. (Clause 3.9.8.2.2)
Q: A circuit connected to an ISOLATED supply shall not exceed how many volts?
A: 500V AC (AS/NZS 3000 Clause 7.4.3)
Q: Can the equipotential bonding conductors connected between socket outlets of an ISOLATED circuit be connected to the equipotential bond of the MEN system?
A: No (AS/NZS 3000 Clause 7.4.6)
Q: What are the minimum values of Insulation Resistance for a circuit connected to an ISOLATED supply? (AS/NZS 3000 Clause 7.4.8.1)
A:
Between transformer primary and secondary windings: 1 MΩ
Between isolated circuit active conductors and earth: 1 MΩ
Between isolated circuit equipotential bonding and transformer primary earthing: 1 MΩ
Q: What resistance should be measured between the equipotentially bonded earth pins of multiple socket outlets on an ISOLATED circuit?
A: 0.5 Ω (AS/NZS 3000 Clause 7.4.8.4)
Q: What are the requirements for a functional switch for an electric cooktop, and where must it be located?
A: It must be within 2 m of the appliance and disconnect all active wires. (AS/NZS 3000 Clause 4.7.1)
Q: Can the main switch for a pump operating the fire sprinkler system be installed downstream of the general services main switch?
A: No (AS/NZS 3000 Clause 7.2.5.4)
Q: What are the three major risks that the AS/NZS 3000 principles are designed to protect against?
A:
Shock current
Excessive temperatures
Explosion
Q: Refer to clause 1.4.35 - What is indirect contact?
A: Contact with conductive parts that are not live under normal conditions.
Q: List 2 fault conditions that may cause conductive parts of electrical equipment to become ‘live’.
A:
Insulation failure
Broken wire
Q: List 4 electrical items that may cause electric shock from indirect contact.
A:
Exposed conductive parts of home appliances
Conductive floor or metal structure
Support railings or similar fixtures
Distribution boards
Q: Refer to clause 1.4.78 – What does fault protection aim to prevent?
A: Electric shock or hazard
Q: Refer to clause 1.5.5.2 – What are methods of protection against indirect contact?
A:
Automatic disconnection of power supply
Use of Class II equipment
Separation (isolated supply)
Limiting fault current
Q: What is the minimum horizontal distance for a non-IP rated socket outlet next to a bath?
A: 0.6 meters
Q: What is the minimum horizontal distance for a non-IP rated light switch next to a bath?
A: 0.3 meters
Q: To what horizontal distance does Zone 2 extend from a bath without a barrier?
A: 0.6 meters
Q: What is the minimum horizontal distance for a non-IP rated socket outlet next to a shower screen?
A: 0.6 meters
Q: To what vertical distance does Zone 2 extend above a shower base without a fixed barrier?
A: 2.5 meters
Q: What is the minimum horizontal distance for a non-IP rated socket outlet next to a hand basin <45L?
A: 0.15 meters
Q: What is the minimum vertical distance above a bathroom floor for a non-IP rated socket outlet?
A: No specific minimum if outside all zones
Q: What is the minimum horizontal distance for a non-IP rated socket outlet next to a kitchen sink <45L?
A: 0.15 meters
Q: What is the minimum horizontal distance for a non-IP rated socket outlet next to a laundry tub >45L?
A: 0.15 meters
Q: What is Zone 0 of an in-ground swimming pool?
A: Interior of the pool including water, walls, and floor
Q: To what horizontal distance does Zone 1 extend from a pool’s edge?
A: 2 meters horizontally, 2.5 meters vertically
Q: Can you install an IP53 10A socket outlet 1.5m from the pool’s rim to supply a pump (without further enclosure)?
A: No
Q: Can a 230V light fitting be installed 2.1m from the pool’s edge?
A: No
Q: Is a 4000L water container considered a pool or spa?
A: Spa pool or tub
Q: What are the requirements for pool lights in Zone 0?
A:
Supply not exceeding 12V AC or 30V ripple-free DC
Safety isolating transformer
Minimum IPX8 rating
Q: What is the minimum cross-sectional area (CSA) of the equipotential bonding conductor required for bonding conductive reinforcing in concrete floors or walls in rooms with a shower or bath?
A: 4 mm²
Q: Refer to clause 5.6.2.6 – What items around swimming and spa pools must be equipotentially bonded?
A:
(a) Exposed conductive parts of any electrical equipment in the classified pool zones
(b) Exposed conductive parts of equipment not double insulated and in contact with pool water or its circulation/filtering system
Bonding shall also extend to:
(i) Extraneous conductive parts of the pool structure, including reinforced metal of the shell and deck
(ii) Conductive fittings such as ladders and diving boards
(iii) Fixed conductive material within arm’s reach of the pool edge, such as fences, lamp standards, and pipework
Q: What is the minimum CSA of the equipotential bonding conductor in these cases?
A: 4 mm²
Q: What is the minimum IP rating required for a socket outlet in bathroom Zone 0?
A: (d) Socket outlets are not permitted in Zone 0
Q: Underwater pool lighting may be supplied with which of the following options?
A:
(a) A PELV or SELV supply of 12 V AC or less
(b) An SELV system not exceeding 30 V DC
(Correct answers: (a) and (b) are compliant)
Q: When protection against indirect contact is provided by automatic disconnection, what are the maximum disconnection times?
A: AS/NZS 3000 Reference: Clause 1.5.5.3(d)
(a) Power circuit < 63A: 0.4 seconds
(b) Equipment with only single insulation: 0.4 seconds
(c) Electric range: 5 seconds
(d) Submain: 5 seconds 
Q: What are the limits of “touch voltage” requiring disconnection of supply?
A: 50V AC or 120V DC
AS/NZS 3000 Reference: Clause 1.5.5.1(d)
Q: What are four acceptable methods of protection against indirect contact as per AS/NZS 3000:2007 Clause 1.5.5.1?
A:
Automatic disconnection of supply
Use of Class II equipment
Electrical separation (Isolated supply)
Limiting fault current
Q: Protection against indirect contact by automatic disconnection of the supply is achieved by two factors. What are the two factors?
A:
Fuse or Circuit breaker
Timely disconnection upon fault (within required disconnection time limits)
AS/NZS 3000 Reference: Clause 2.5.2
Q: Where may socket outlets be installed in a pool zone for the connection of pool equipment?
A:
In Zone 1, only for pool equipment and subject to limitations stated in Table 6.2
AS/NZS 3000 Reference: Table 6.2
Q: Describe one method of supply for luminaires immersed in pool water.
A:
Supply must be IPX8 rated
Voltage limited to 12V AC or 30V ripple-free DC
Supplied by SELV or PELV with no earth connection
AS/NZS 3000 Reference: Table 6.2
Q: State two alternative supply requirements for a circuit that supplies a pool filter pump.
A:
Option 1: Use SELV or PELV system
Option 2: Use RCD protection for the supply circuit
AS/NZS 3000 Reference: Clause 6.3.4.3
Q. Is it permissible to install unenclosed socket outlets within zones 1 or 2 of a bathroom?
A:
Zone 2: Yes, but only shaver outlets or RCD-protected outlets in cupboards.
Zone 3: RCD protection is required.
AS/NZS 3000 Reference: Table 6.1
Q12. Complete the following table. Indicate the minimum IP rating of accessories permitted in the following locations:
Q13. Complete the following table by determining the minimum horizontal clearance between a normal socket outlet and the following water containers:
Q: What are the two main risks that an earthing system protects against in the event of insulation breakdown?
A:
Fault current
Earth leakage current
Q: What happens in an effective earthing system when there are exposed conductive parts?
A: Exposed conductive parts are electrically connected to the general mass of earth, forming part of the earthing system network in the distribution area.
Q: Define "Exposed Conductive Part" according to AS/NZS 3000 Clause 1.4.62.
A: An exposed conductive part is a part of electrical equipment which is normally accessible but not live under normal conditions, and may become live under fault conditions.
Q: Define "Extraneous Conductive Part" according to AS/NZS 3000 Clause 1.4.63.
A: An extraneous conductive part is a conductive part that does not form part of the electrical installation but may be at earth potential.
Q: List 2 examples of extraneous conductive parts.
A:
Metal water, waste water, gas pipe lines
Cooling or heating systems
Q1. What is the fundamental safety principle of earthing in electrical installations?
A: Protection of person and equipment against dangers from indirect contact with exposed conductive parts.
Q2. What is provided by earthing to stabilize potential with respect to earth?
A: Leakage current path
Q3. Define "readily accessible" as per AS/NZS 3000 Clause 1.4.3.
A: An object is deemed readily accessible if it can be reached quickly and easily, and is less than 2 metres above the ground, floor, or platform.
Q4. Define "Earthed" as per Clause 1.4.47.
A: Any equipment or conductor connected to the general mass of earth is deemed to be earthed.
Q5. Define an "Earthed situation" as per Clause 1.4.48.
A: A location where a person can simultaneously touch exposed conductive parts and any other material (like floor) that may provide a path to earth.
Q6. List examples of earthed situations:
A:
All parts of a bathroom, laundry, lavatory, toilet, or kitchen
Outdoor equipment mounted within 2.5 m of the ground
Rooms with sockets where contact with exposed parts and conductive surfaces is possible within 2.5 m
Any direction within 2.5 m of a conductive floor
Q7. List three examples of conductive floor materials:
A:
Earth
Concrete
Tile
Q1. What is the definition of a main earthing conductor according to AS/NZS 3000 clause 1.4.81?
A: The main earthing conductor is connected between the main earthing terminal or bar to the earth electrode.
Q2. What is the required insulation colour for the main earthing conductor as per Clause 3.8.1?
A: Green/yellow
Q3. What is the minimum allowable size for a copper main earthing conductor?
A: 4 mm² (Clause 5.3.3.2)
Q3. What is the minimum allowable size for a copper main earthing conductor?
A: 4 mm² (Clause 5.3.3.2)
Q5. What clause covers the connection of the main earthing conductor to the earth electrode?
A: Clause 5.5.1.2
Q6. When connecting the main earthing conductor to the earth electrode, what conditions must be satisfied?
A:
Earth electrode must be compatible with surrounding soil and protected against corrosion.
Continuity must be tested if the electrode is not visible after installation.
Connection must be made using an approved method (e.g. clamps or welding).
Location and resistance must meet the conditions specified in Clause 5.5.2 and Clause 5.6.4.""")
