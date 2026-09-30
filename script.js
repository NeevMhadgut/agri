/* =========================================================
   script.js - JavaScript Programming & Form Validation
   Use Case: Smart Irrigation Advisory Web Portal (KJS-AGR-01)
   Covers Experiments 4 & 5
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {
  // =========================================================
  // EXPERIMENT 4: Form Validation Implementation
  // =========================================================
  const regForm = document.getElementById("farmerRegistrationForm");
  const successBox = document.getElementById("formSuccessMsg");

  if (regForm) {
    // Individual field validation functions
    function validateFarmerName() {
      const field = document.getElementById("farmerName");
      const err = document.getElementById("farmerNameError");
      const val = field.value.trim();
      const nameRegex = /^[A-Za-z\s]+$/;

      if (val === "") {
        setError(field, err, "Farmer Name is required and cannot be blank.");
        return false;
      } else if (!nameRegex.test(val)) {
        setError(field, err, "Farmer Name must contain alphabetic characters and spaces only.");
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validateMobile() {
      const field = document.getElementById("mobileNumber");
      const err = document.getElementById("mobileNumberError");
      const val = field.value.trim();
      const mobileRegex = /^[6-9]\d{9}$/;

      if (val === "") {
        setError(field, err, "Mobile Number is required.");
        return false;
      } else if (!mobileRegex.test(val)) {
        setError(field, err, "Mobile Number must be exactly 10 digits starting with 6-9.");
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validateEmail() {
      const field = document.getElementById("email");
      const err = document.getElementById("emailError");
      const val = field.value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (val === "") {
        setError(field, err, "Email Address is required.");
        return false;
      } else if (!emailRegex.test(val)) {
        setError(field, err, "Enter a valid email format (e.g., farmer@example.com).");
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validatePlotId() {
      const field = document.getElementById("plotId");
      const err = document.getElementById("plotIdError");
      const val = field.value.trim().toUpperCase();
      field.value = val;
      const plotRegex = /^AGR-\d{4}$/;

      if (val === "") {
        setError(field, err, "Plot ID is required.");
        return false;
      } else if (!plotRegex.test(val)) {
        setError(field, err, "Plot ID must follow format AGR-1234.");
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validateVillage() {
      const field = document.getElementById("village");
      const err = document.getElementById("villageError");
      const val = field.value.trim();

      if (val === "") {
        setError(field, err, "Village name is required.");
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validateDropdown(fieldId, errorId, fieldName) {
      const field = document.getElementById(fieldId);
      const err = document.getElementById(errorId);
      if (!field.value || field.value === "") {
        setError(field, err, `Please select a valid ${fieldName}.`);
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validateMoisture() {
      const field = document.getElementById("soilMoisture");
      const err = document.getElementById("soilMoistureError");
      const val = parseFloat(field.value);

      if (isNaN(val) || field.value.trim() === "") {
        setError(field, err, "Soil Moisture is required.");
        return false;
      } else if (val < 0 || val > 100) {
        setError(field, err, "Soil Moisture must be between 0% and 100%.");
        return false;
      }
      clearError(field, err);
      return true;
    }

    function validateRegistrationDate() {
      const field = document.getElementById("registrationDate");
      const err = document.getElementById("registrationDateError");
      const val = field.value;

      if (!val) {
        setError(field, err, "Registration Date is required.");
        return false;
      }
      const selectedDate = new Date(val);
      const today = new Date();
      today.setHours(23, 59, 59, 999);

      if (selectedDate > today) {
        setError(field, err, "Registration Date cannot be a future date.");
        return false;
      }
      clearError(field, err);
      return true;
    }

    // Helpers
    function setError(field, errElement, message) {
      field.classList.add("is-invalid");
      field.classList.remove("is-valid");
      if (errElement) errElement.textContent = message;
    }

    function clearError(field, errElement) {
      field.classList.remove("is-invalid");
      field.classList.add("is-valid");
      if (errElement) errElement.textContent = "";
    }

    // Attach blur event listeners for real-time validation feedback
    document.getElementById("farmerName").addEventListener("blur", validateFarmerName);
    document.getElementById("mobileNumber").addEventListener("blur", validateMobile);
    document.getElementById("email").addEventListener("blur", validateEmail);
    document.getElementById("plotId").addEventListener("blur", validatePlotId);
    document.getElementById("village").addEventListener("blur", validateVillage);
    document.getElementById("soilMoisture").addEventListener("blur", validateMoisture);
    document.getElementById("registrationDate").addEventListener("blur", validateRegistrationDate);
    document.getElementById("cropStage").addEventListener("change", () => validateDropdown("cropStage", "cropStageError", "Crop Stage"));
    document.getElementById("soilType").addEventListener("change", () => validateDropdown("soilType", "soilTypeError", "Soil Type"));
    document.getElementById("irrigationMethod").addEventListener("change", () => validateDropdown("irrigationMethod", "irrigationMethodError", "Irrigation Method"));

    // Form Submit Event Handling
    regForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const isNameValid = validateFarmerName();
      const isMobileValid = validateMobile();
      const isEmailValid = validateEmail();
      const isPlotValid = validatePlotId();
      const isVillageValid = validateVillage();
      const isCropValid = validateDropdown("cropStage", "cropStageError", "Crop Stage");
      const isSoilValid = validateDropdown("soilType", "soilTypeError", "Soil Type");
      const isMethodValid = validateDropdown("irrigationMethod", "irrigationMethodError", "Irrigation Method");
      const isMoistureValid = validateMoisture();
      const isDateValid = validateRegistrationDate();

      const formIsValid = isNameValid && isMobileValid && isEmailValid && isPlotValid &&
                          isVillageValid && isCropValid && isSoilValid && isMethodValid &&
                          isMoistureValid && isDateValid;

      if (!formIsValid) {
        if (successBox) successBox.style.display = "none";
        alert("Please correct the highlighted errors before submitting the form.");
        return;
      }

      // Success
      if (successBox) {
        const farmerName = document.getElementById("farmerName").value.trim();
        const plotId = document.getElementById("plotId").value.trim();
        successBox.innerHTML = `<strong>Registration Successful!</strong> Farmer <em>${farmerName}</em> with Plot ID <em>${plotId}</em> has been registered in the Smart Irrigation Advisory Portal.`;
        successBox.style.display = "block";
        successBox.scrollIntoView({ behavior: "smooth" });
      } else {
        alert("Registration Successful!");
      }
    });

    // Reset button handler
    regForm.addEventListener("reset", function () {
      setTimeout(() => {
        const inputs = regForm.querySelectorAll("input, select");
        inputs.forEach(el => {
          el.classList.remove("is-valid", "is-invalid");
        });
        const errs = regForm.querySelectorAll(".error-msg");
        errs.forEach(err => err.textContent = "");
        if (successBox) successBox.style.display = "none";
      }, 50);
    });
  }

  // =========================================================
  // EXPERIMENT 5: JavaScript Programming Modules
  // =========================================================

  // Task 1: Soil Moisture Deficit Calculator
  const calcBtn = document.getElementById("btnCalcMoisture");
  if (calcBtn) {
    calcBtn.addEventListener("click", function () {
      const farmerName = document.getElementById("calcFarmerName").value.trim() || "Ramesh Patil";
      const plotId = document.getElementById("calcPlotId").value.trim() || "AGR-1024";
      const currentMoisture = parseFloat(document.getElementById("calcCurrentMoisture").value);
      const requiredMoisture = parseFloat(document.getElementById("calcRequiredMoisture").value);

      if (isNaN(currentMoisture) || isNaN(requiredMoisture)) {
        alert("Please enter valid numeric moisture levels.");
        return;
      }

      const deficit = requiredMoisture - currentMoisture;
      let statusMsg = "";
      if (deficit > 0) {
        // Approximate 25 liters per 1% deficit per square meter
        const waterPerSqM = (deficit * 0.8).toFixed(1);
        statusMsg = `Farmer: ${farmerName} | Plot: ${plotId}\n` +
                    `Current Moisture: ${currentMoisture}%\n` +
                    `Target Moisture: ${requiredMoisture}%\n` +
                    `Moisture Deficit: ${deficit.toFixed(1)}%\n` +
                    `Water Required: ~${waterPerSqM} liters/m² to restore root-zone field capacity.`;
      } else {
        statusMsg = `Farmer: ${farmerName} | Plot: ${plotId}\n` +
                    `Current Moisture: ${currentMoisture}%\n` +
                    `Target Moisture: ${requiredMoisture}%\n` +
                    `No moisture deficit detected. Soil is sufficiently hydrated.`;
      }

      // Display alert()
      alert("Irrigation Advisory Status:\n" + statusMsg);

      // Display in DOM
      const outBox = document.getElementById("calcMoistureOutput");
      if (outBox) {
        outBox.innerHTML = `<div class="card" style="background:#e8f5e9; border:1px solid #74c69d;">
          <h4 style="margin:0 0 0.5rem; color:#1b4332;">Task 1 Result: Moisture Deficit Calculation</h4>
          <p><strong>Farmer:</strong> ${farmerName} | <strong>Plot ID:</strong> ${plotId}</p>
          <p><strong>Current Soil Moisture:</strong> ${currentMoisture}% | <strong>Required Moisture:</strong> ${requiredMoisture}%</p>
          <p><strong>Moisture Deficit:</strong> ${deficit > 0 ? deficit.toFixed(1) + '%' : '0% (Optimal)'}</p>
          <p><strong>Status:</strong> ${deficit > 0 ? '<span style="color:#d90429; font-weight:bold;">Deficit Alert: Irrigation Recommended</span>' : '<span style="color:#2b9348; font-weight:bold;">Adequate Hydration</span>'}</p>
        </div>`;
      }
    });
  }

  // Task 2: Rule-Based Recommendation Engine
  const evalRuleBtn = document.getElementById("btnEvalRules");
  if (evalRuleBtn) {
    evalRuleBtn.addEventListener("click", function () {
      const soilMoisture = parseFloat(document.getElementById("ruleSoilMoisture").value);
      const rainExpected = document.getElementById("ruleRainForecast").value === "yes";
      const cropStage = document.getElementById("ruleCropStage").value;

      if (isNaN(soilMoisture)) {
        alert("Please enter a valid soil moisture percentage.");
        return;
      }

      let recommendation = "";
      let alertClass = "";

      if (rainExpected) {
        recommendation = "Postpone Irrigation (Rain expected in weather forecast)";
        alertClass = "status-hold";
      } else if (soilMoisture < 30) {
        recommendation = "Irrigation Required Immediately";
        alertClass = "status-hold";
      } else if (soilMoisture >= 30 && soilMoisture <= 50) {
        recommendation = "Monitor Soil Moisture";
        alertClass = "status-monitor";
      } else {
        recommendation = "Irrigation Not Required";
        alertClass = "status-approved";
      }

      const outBox = document.getElementById("ruleOutput");
      if (outBox) {
        outBox.innerHTML = `<div class="card" style="margin-top:1rem; border-left:4px solid #2d6a4f;">
          <h4 style="margin:0 0 0.5rem;">Task 2 Result: Advisory Recommendation</h4>
          <p><strong>Input Parameters:</strong> Soil Moisture = ${soilMoisture}%, Rain Forecast = ${rainExpected ? "Rain Expected" : "Clear Weather"}, Crop Stage = ${cropStage}</p>
          <p><strong>Advisory Action:</strong> <span class="status-pill ${alertClass}">${recommendation}</span></p>
        </div>`;
      }
    });
  }

  // Task 3: Sugarcane Farm Object
  const farmObjBtn = document.getElementById("btnFarmObject");
  if (farmObjBtn) {
    farmObjBtn.addEventListener("click", function () {
      const sugarcaneFarm = {
        farmerName: "Sanjay More",
        plotId: "AGR-3052",
        cropStage: "Grand Growth",
        soilMoisture: 26.5,
        area: "4.5 Acres",
        pumpStatus: "Active",
        displayFarmInfo: function () {
          return `
            <div class="card" style="background:#f4f9f4; border:1px solid #95d5b2;">
              <h4 style="color:#1b4332; margin-top:0;">Sugarcane Farm Object Record</h4>
              <ul style="list-style:none; padding-left:0; margin:0;">
                <li><strong>Farmer Name:</strong> ${this.farmerName}</li>
                <li><strong>Plot ID:</strong> ${this.plotId}</li>
                <li><strong>Crop Stage:</strong> ${this.cropStage}</li>
                <li><strong>Soil Moisture:</strong> ${this.soilMoisture}%</li>
                <li><strong>Farm Area:</strong> ${this.area}</li>
                <li><strong>Irrigation Pump Status:</strong> <span class="badge ${this.pumpStatus === 'Active' ? 'urgent' : ''}">${this.pumpStatus}</span></li>
              </ul>
            </div>
          `;
        }
      };

      const outBox = document.getElementById("farmObjectOutput");
      if (outBox) {
        outBox.innerHTML = sugarcaneFarm.displayFarmInfo();
      }
    });
  }

  // Task 4: Hourly Sensor Readings Analysis with Arrays
  const sensorArrayBtn = document.getElementById("btnAnalyzeSensors");
  if (sensorArrayBtn) {
    sensorArrayBtn.addEventListener("click", function () {
      // 24-hour moisture readings from smart field sensor
      const sensorReadings = [38, 35, 33, 30, 28, 27, 26, 25, 29, 32, 34, 36, 35, 33, 31, 29, 28, 27, 26, 25, 24, 28, 31, 35];

      // 1. All readings
      const allReadingsStr = sensorReadings.join("%, ") + "%";

      // 2. Minimum
      const minMoisture = Math.min(...sensorReadings);

      // 3. Maximum
      const maxMoisture = Math.max(...sensorReadings);

      // 4. Average
      const sum = sensorReadings.reduce((acc, curr) => acc + curr, 0);
      const avgMoisture = (sum / sensorReadings.length).toFixed(2);

      // 5. Readings below critical value (critical = 30%)
      const criticalThreshold = 30;
      const criticalCount = sensorReadings.filter(val => val < criticalThreshold).length;

      const outBox = document.getElementById("sensorArrayOutput");
      if (outBox) {
        outBox.innerHTML = `
          <div class="card" style="background:#ffffff; border:1px solid #d8ddd4;">
            <h4 style="color:#1b4332; margin-top:0;">Task 4: Hourly Soil Moisture Sensor Array Analysis</h4>
            <p><strong>1. Hourly Readings (24 Hours):</strong><br><small style="word-break:break-all; color:#374151;">${allReadingsStr}</small></p>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:1rem; margin-top:1rem;">
              <div style="padding:0.75rem; background:#f0fdf4; border-radius:6px; border:1px solid #bbf7d0;">
                <div style="font-size:0.8rem; color:#166534; font-weight:600;">MINIMUM MOISTURE</div>
                <div style="font-size:1.4rem; font-weight:700; color:#15803d;">${minMoisture}%</div>
              </div>
              <div style="padding:0.75rem; background:#eff6ff; border-radius:6px; border:1px solid #bfdbfe;">
                <div style="font-size:0.8rem; color:#1e40af; font-weight:600;">MAXIMUM MOISTURE</div>
                <div style="font-size:1.4rem; font-weight:700; color:#1d4ed8;">${maxMoisture}%</div>
              </div>
              <div style="padding:0.75rem; background:#fefce8; border-radius:6px; border:1px solid #fef08a;">
                <div style="font-size:0.8rem; color:#854d0e; font-weight:600;">AVERAGE MOISTURE</div>
                <div style="font-size:1.4rem; font-weight:700; color:#a16207;">${avgMoisture}%</div>
              </div>
              <div style="padding:0.75rem; background:#fef2f2; border-radius:6px; border:1px solid #fecaca;">
                <div style="font-size:0.8rem; color:#991b1b; font-weight:600;">CRITICAL READINGS (<30%)</div>
                <div style="font-size:1.4rem; font-weight:700; color:#b91c1c;">${criticalCount} hours</div>
              </div>
            </div>
          </div>
        `;
      }
    });
  }

  // Task 5: JavaScript Input Validation Suite
  const runValSuiteBtn = document.getElementById("btnRunValidationSuite");
  if (runValSuiteBtn) {
    runValSuiteBtn.addEventListener("click", function () {
      const name = document.getElementById("valTestName").value.trim();
      const mobile = document.getElementById("valTestMobile").value.trim();
      const plotId = document.getElementById("valTestPlotId").value.trim().toUpperCase();
      const moisture = parseFloat(document.getElementById("valTestMoisture").value);

      const isNameValid = /^[A-Za-z\s]+$/.test(name) && name.length > 0;
      const isMobileValid = /^[6-9]\d{9}$/.test(mobile);
      const isPlotValid = /^AGR-\d{4}$/.test(plotId);
      const isMoistureValid = !isNaN(moisture) && moisture >= 0 && moisture <= 100;

      const outBox = document.getElementById("validationSuiteOutput");
      if (outBox) {
        outBox.innerHTML = `
          <div class="card" style="background:#f8fafc; border:1px solid #cbd5e1;">
            <h4 style="color:#0f172a; margin-top:0;">Task 5: JavaScript Validation Test Suite Results</h4>
            <table class="data-table" style="font-size:0.88rem; width:100%;">
              <thead>
                <tr>
                  <th>Field</th>
                  <th>Input Value</th>
                  <th>Rule Specification</th>
                  <th>Validation Result</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Farmer Name</td>
                  <td><code>${name || "(empty)"}</code></td>
                  <td>Alphabetic characters &amp; spaces only (/^[A-Za-z\\s]+$/)</td>
                  <td>${isNameValid ? '<span class="status-pill status-approved">PASS - Valid</span>' : '<span class="status-pill status-hold">FAIL - Invalid</span>'}</td>
                </tr>
                <tr>
                  <td>Mobile Number</td>
                  <td><code>${mobile || "(empty)"}</code></td>
                  <td>10 digits starting with 6-9 (/^[6-9]\\d{9}$/)</td>
                  <td>${isMobileValid ? '<span class="status-pill status-approved">PASS - Valid</span>' : '<span class="status-pill status-hold">FAIL - Invalid</span>'}</td>
                </tr>
                <tr>
                  <td>Plot ID</td>
                  <td><code>${plotId || "(empty)"}</code></td>
                  <td>Format AGR-#### (/^AGR-\\d{4}$/)</td>
                  <td>${isPlotValid ? '<span class="status-pill status-approved">PASS - Valid</span>' : '<span class="status-pill status-hold">FAIL - Invalid</span>'}</td>
                </tr>
                <tr>
                  <td>Soil Moisture</td>
                  <td><code>${isNaN(moisture) ? "(NaN)" : moisture + "%"}</code></td>
                  <td>Numeric range between 0% and 100%</td>
                  <td>${isMoistureValid ? '<span class="status-pill status-approved">PASS - Valid</span>' : '<span class="status-pill status-hold">FAIL - Invalid</span>'}</td>
                </tr>
              </tbody>
            </table>
          </div>
        `;
      }
    });
  }

  // Task 6: Interactive Advisory Request & Registration Form
  const exp5Form = document.getElementById("exp5RequestForm");
  if (exp5Form) {
    exp5Form.addEventListener("submit", function (e) {
      e.preventDefault();

      const nameField = document.getElementById("reqFarmerName");
      const mobileField = document.getElementById("reqMobile");
      const plotField = document.getElementById("reqPlotId");
      const moistureField = document.getElementById("reqMoisture");
      const stageField = document.getElementById("reqCropStage");
      const dateField = document.getElementById("reqDate");

      const nameVal = nameField.value.trim();
      const mobileVal = mobileField.value.trim();
      const plotVal = plotField.value.trim().toUpperCase();
      plotField.value = plotVal;
      const moistureVal = parseFloat(moistureField.value);
      const stageVal = stageField.value;
      const dateVal = dateField.value;

      let valid = true;
      if (!/^[A-Za-z\s]+$/.test(nameVal)) {
        document.getElementById("reqFarmerNameErr").textContent = "Name must be letters & spaces only.";
        nameField.classList.add("is-invalid");
        valid = false;
      } else {
        document.getElementById("reqFarmerNameErr").textContent = "";
        nameField.classList.remove("is-invalid");
        nameField.classList.add("is-valid");
      }

      if (!/^[6-9]\d{9}$/.test(mobileVal)) {
        document.getElementById("reqMobileErr").textContent = "Must be 10 digits starting with 6-9.";
        mobileField.classList.add("is-invalid");
        valid = false;
      } else {
        document.getElementById("reqMobileErr").textContent = "";
        mobileField.classList.remove("is-invalid");
        mobileField.classList.add("is-valid");
      }

      if (!/^AGR-\d{4}$/.test(plotVal)) {
        document.getElementById("reqPlotIdErr").textContent = "Plot ID must follow format AGR-####.";
        plotField.classList.add("is-invalid");
        valid = false;
      } else {
        document.getElementById("reqPlotIdErr").textContent = "";
        plotField.classList.remove("is-invalid");
        plotField.classList.add("is-valid");
      }

      if (isNaN(moistureVal) || moistureVal < 0 || moistureVal > 100) {
        document.getElementById("reqMoistureErr").textContent = "Moisture must be between 0 and 100.";
        moistureField.classList.add("is-invalid");
        valid = false;
      } else {
        document.getElementById("reqMoistureErr").textContent = "";
        moistureField.classList.remove("is-invalid");
        moistureField.classList.add("is-valid");
      }

      if (!dateVal) {
        document.getElementById("reqDateErr").textContent = "Date is required.";
        dateField.classList.add("is-invalid");
        valid = false;
      } else {
        document.getElementById("reqDateErr").textContent = "";
        dateField.classList.remove("is-invalid");
        dateField.classList.add("is-valid");
      }

      if (!valid) return;

      const successBox = document.getElementById("task6SuccessMsg");
      if (successBox) {
        successBox.innerHTML = `<strong>Advisory Request Submitted Successfully!</strong><br>Record generated for Farmer <strong>${nameVal}</strong> (Plot: <strong>${plotVal}</strong>) on ${dateVal}.`;
        successBox.style.display = "block";
      }

      const outBox = document.getElementById("exp5RequestOutput");
      if (outBox) {
        const quotaMins = moistureVal < 30 ? 45 : (moistureVal < 45 ? 25 : 0);
        outBox.innerHTML = `
          <div class="card" style="background:#f0fdf4; border:1px solid #86efac; margin-top:1rem;">
            <h4 style="color:#166534; margin-top:0;">Task 6 Generated Advisory Decision</h4>
            <p><strong>Farmer:</strong> ${nameVal} | <strong>Mobile:</strong> ${mobileVal} | <strong>Plot:</strong> ${plotVal}</p>
            <p><strong>Stage:</strong> ${stageVal} | <strong>Telemetry Moisture:</strong> ${moistureVal}%</p>
            <p><strong>Recommended Action:</strong> ${quotaMins > 0 ? `<span class="status-pill status-hold">Irrigate ${quotaMins} minutes via drip</span>` : '<span class="status-pill status-approved">Adequate soil moisture - No irrigation needed today</span>'}</p>
          </div>
        `;
      }
    });
  }
});
