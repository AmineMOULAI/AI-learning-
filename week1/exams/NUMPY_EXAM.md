# 🎓 NUMPY MASTERY EXAM
## Mini-Project Assessment (Exam Date: Jan 15, 2026)

**Student**: You (L3 CS)  
**Topic**: NumPy Fundamentals (Arrays, Slicing, Operations, Broadcasting)  
**Duration**: 1h30min maximum  
**Total Score**: /20  

---

## 📋 INSTRUCTIONS

1. **Read the entire exam first** (5 min) – then start coding
2. **Create file**: `week1/exam_numpy_mastery.py`
3. **Write clean code** with comments for each section
4. **Test your code** – all outputs must be correct
5. **Submit**: Push to GitHub with commit message: `"Week1 Exam: NumPy Mastery Assessment"`

---

## 🎯 PART 1: Array Creation & Inspection (4 points)

**Problem**: You are given raw temperature data from 4 weather stations across 7 days.

```
Station 1: [22.5, 23.1, 21.8, 20.2, 19.5, 18.9, 19.2]
Station 2: [15.3, 15.8, 16.2, 14.9, 14.1, 13.7, 14.0]
Station 3: [28.5, 29.1, 28.8, 27.3, 26.5, 25.9, 26.2]
Station 4: [10.2, 11.5, 12.1, 11.8, 10.5, 9.8, 10.1]
```

### 1.1 Create a 2D NumPy array (1pt)
- Create a 2D array `temperatures` where rows are stations and columns are days
- Print the array

### 1.2 Print array dimensions (1pt)
- Print how many dimensions the array has
- Print the shape (rows × columns)
- Print the total number of elements

### 1.3 Calculate basic statistics (1pt)
- Print the mean temperature across all stations and days
- Print the minimum temperature
- Print the maximum temperature

### 1.4 Data type and size (1pt)
- Print the data type of the array
- Print total number of elements

---

## 🎯 PART 2: Indexing & Slicing (5 points)

**Context**: Extract specific data from the temperature array.

### 2.1 Single element access (1pt)
- Get the temperature at Station 3, Day 5 (using 0-based indexing)
- Print it with a clear label

### 2.2 Row extraction (1pt)
- Extract all temperatures for Station 2 (all 7 days)
- Print the extracted row

### 2.3 Column extraction (1pt)
- Extract all temperatures for Day 4 (all 4 stations)
- Print the extracted column

### 2.4 Sub-array extraction (1pt)
- Extract temperatures for Stations 1-2 and Days 2-5
- Print the shape of this sub-array
- Print the values

### 2.5 Advanced slicing with step (1pt)
- Extract all temperatures for odd-numbered days only (days 1, 3, 5 in 0-based indexing)
- For all stations
- Print the shape and values
- *Hint: Step notation might help*

---

## 🎯 PART 3: Operations & Broadcasting (6 points)

**Context**: Process and transform the temperature data.

### 3.1 Temperature conversion (1pt)
- Convert all temperatures from Celsius to Fahrenheit using: `F = C × 9/5 + 32`
- **Do NOT use loops** – use NumPy vectorized operations
- Create array `temps_fahrenheit`
- Print the first station's converted temperatures

### 3.2 Normalization (1pt)
- Normalize all temperatures using: `normalized = (data - mean) / std`
- Calculate the mean and standard deviation of original temperatures
- Create `temps_normalized` using the formula
- Print the mean and std of the normalized array (should be close to 0 and 1)

### 3.3 Find anomalies (1pt)
- Create a boolean mask for temperatures **above 25°C**
- Count how many temperature values exceed 25°C
- Print the count

### 3.4 Row-wise mean (1pt)
- Calculate the mean temperature **for each station** (across all days)
- Result should have 4 values (one per station)
- Print these 4 values

### 3.5 Column-wise normalization (1pt)
- Normalize each day independently
- For each day: `(day_temps - day_mean) / day_std`
- Create array `temps_column_normalized`
- Print the shape to verify it's correct

### 3.6 Broadcasting challenge (1pt)
- You want to reduce all temperatures by a different amount for each station:
  - Station 1: reduce by 1°C
  - Station 2: reduce by 0.5°C
  - Station 3: reduce by 2°C
  - Station 4: reduce by 0.2°C
- Create an array with these reduction values
- Subtract from original temperatures using **broadcasting**
- Print the result
- *Hint: Shape matters for broadcasting to work*

---

## 🎯 PART 4: Real-world Application (5 points)

**Problem**: Analyze weather data and generate insights.

### 4.1 Identify coldest station (1pt)
- Find which station has the **lowest mean temperature** across all days
- Print the station number and its mean temperature

### 4.2 Identify warmest day (1pt)
- Find which day had the **highest mean temperature** across all stations
- Print the day number and its mean temperature

### 4.3 Temperature variability (1pt)
- For each station, calculate the **standard deviation** (how much temperatures vary across days)
- Print for each station: `"Station X: {std_value}°C"`

### 4.4 Create summary statistics table (1pt)
- For each station, calculate: Mean, Min, Max, Std
- Print a nicely formatted summary
- Example:
  ```
  Station 1 | Mean: 21.17 | Min: 18.9 | Max: 23.1 | Std: 1.54
  Station 2 | Mean: 15.0  | Min: 13.7 | Max: 16.2 | Std: 1.01
  ```

### 4.5 Identify day with extreme variation (1pt)
- For each day, calculate how much temperatures vary **across stations**
- Find the day with the **highest variation** (highest standard deviation)
- Print the day number and its variation value

---

## 📊 GRADING RUBRIC (Score /20)

| Part | Category | Criteria | Points |
|------|----------|----------|--------|
| **1** | Fundamentals | Array creation correct, dimensions printed, statistics accurate | 4 |
| **2** | Indexing & Slicing | All 5 slicing operations work correctly | 5 |
| **3** | Operations | All 6 operations implemented, vectorized (no loops), correct results | 6 |
| **4** | Application | All 5 real-world analyses complete and correct | 5 |

---

## ✅ SUBMISSION CHECKLIST

Before submitting, verify:

- [ ] File name: `exam_numpy_mastery.py`
- [ ] All code runs **without errors**
- [ ] All print statements show clear output
- [ ] Comments explain each section
- [ ] No loops used in Parts 1-3 (NumPy vectorization only)
- [ ] File pushed to GitHub
- [ ] Commit message: `"Week1 Exam: NumPy Mastery Assessment"`

---

## 🏆 GRADING SCALE & INTERPRETATION

| Score | Grade | Assessment |
|-------|-------|------------|
| 18-20 | **A** ⭐ | **Excellent** – Deep understanding, ready for advanced topics |
| 15-17 | **B+** ✅ | **Very Good** – Solid fundamentals, ready for Pandas |
| 12-14 | **B** ✅ | **Good** – Core concepts understood, needs practice |
| 10-11 | **C+** | Acceptable – Review slicing and operations |
| 8-9 | **C** | Needs improvement – Practice more before Pandas |
| <8 | **F** | Not ready – Review Days 1-3 code first |

---

## 💬 PROFESSOR'S NOTES

Based on your Days 1-3 work, you have **good foundations**. This exam will test:

1. **If you understand WHY** slicing works (not just that it does)
2. **If you can think in vectors** (no loops = NumPy mastery)
3. **If you can apply concepts** to real-world problems

**Good luck! You've prepared well.** 🎓

---

## ⏱️ START EXAM

**Start whenever ready. You have 1h30min. Go!** ⏱️
