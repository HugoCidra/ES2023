/**
 * @file This module provides a function to report key web vital metrics using the 'web-vitals' library.
 */

/**
 * Report web vital metrics using the 'web-vitals' library.
 * 
 * When passed a valid performance entry handler, the function will
 * retrieve key web vital metrics, and call the handler for each metric.
 * 
 * @param {Function} onPerfEntry - The handler function to call with each web vital metric.
 */
const reportWebVitals = onPerfEntry => {
  // Ensure the passed handler exists and is a function.
  if (onPerfEntry && onPerfEntry instanceof Function) {
    // Dynamically import the 'web-vitals' library.
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      // Retrieve and report the Cumulative Layout Shift (CLS).
      getCLS(onPerfEntry);
      // Retrieve and report the First Input Delay (FID).
      getFID(onPerfEntry);
      // Retrieve and report the First Contentful Paint (FCP).
      getFCP(onPerfEntry);
      // Retrieve and report the Largest Contentful Paint (LCP).
      getLCP(onPerfEntry);
      // Retrieve and report the Time to First Byte (TTFB).
      getTTFB(onPerfEntry);
    });
  }
};

// Export the reportWebVitals function.
export default reportWebVitals;