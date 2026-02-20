import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
import { getAnalytics, logEvent } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-analytics.js";

const firebaseConfig = {
    apiKey: "AIzaSyC820DRHZVuoONv1BTnXVN0Cg3EDe3XBdU",
    authDomain: "debtcure.firebaseapp.com",
    projectId: "debtcure",
    storageBucket: "debtcure.firebasestorage.app",
    messagingSenderId: "318694633151",
    appId: "1:318694633151:web:07736c7b6e85daf5a4e00a",
    measurementId: "G-T1SSM5TR15"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Listen for custom events dispatched by the application
window.addEventListener('analytics-event', (e) => {
    try {
        if (e && e.detail) {
            const { eventName, params } = e.detail;
            logEvent(analytics, eventName, params);
            console.log(`Firebase Event Tracked: ${eventName}`, params);
        }
    } catch (error) {
        console.error("Firebase Analytics Error:", error);
    }
});
