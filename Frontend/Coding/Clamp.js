// lodash.clamp
// Think about corner case: lower > upper(not given at this time)
// Method 1:
export default function clamp(value, lower, upper) {
    if (value < lower){
      return lower
    } else if (value > upper){
      return upper
    } else {
      return value
    }
  }

// Method 2:
export default function clamp(value, lower, upper) {
    return Math.min(upper,Math.max(value,lower))
  }