/**
 * @param {Function} fn
 * @return {number}
 */

// All function instances have a length property 
// which indicates the number of parameters expected by the function.
// The length property excludes the rest parameter 
// and only includes parameters before the first one with a default value.
export default function functionLength(fn) {
    return fn.length
  }