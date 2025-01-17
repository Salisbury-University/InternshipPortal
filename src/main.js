import ContactPage from "./pages/ContactPage.vue";
import AdminPage from "./pages/admin/AdminPage.vue";
import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import InsertListingPage from "./pages/InsertListingPage.vue";
import AdminListingsPage from "./pages/admin/AdminListingsPage.vue";
import AdminEditListingPage from "./pages/admin/AdminEditListingPage.vue";
import ResetPasswordAuthPage from "./pages/ResetPasswordAuthPage.vue";
import ResetPasswordPage from "./pages/ResetPasswordPage.vue";
import BrowsePage from "./pages/BrowsePage.vue";
import AdminContactInboxView from "./pages/admin/AdminContactInbox.vue";
import AdminNotificationPage from "./pages/admin/AdminNotificationPage.vue";
import AdminViewMessage from "./pages/admin/AdminViewMessage.vue";
import ListingPage from "./pages/ListingPage.vue";

import "tailwindcss/tailwind.css";
import { createApp } from "vue";

const app = createApp({});
app.component("homepage", HomePage);
app.component("adminpage", AdminPage);
app.component("loginpage", LoginPage);
app.component("contactpage", ContactPage);
app.component("insertpage", InsertListingPage);
app.component("listingpage", ListingPage);
app.component("adminlistings", AdminListingsPage);
app.component("admineditlistingpage", AdminEditListingPage);
app.component("resetpasswordauthpage", ResetPasswordAuthPage);
app.component("resetpasswordpage", ResetPasswordPage);
app.component("browsepage", BrowsePage);
app.component("contactinboxpage", AdminContactInboxView);
app.component("notificationpage", AdminNotificationPage);
app.component("adminviewmessagepage", AdminViewMessage);

app.config.compilerOptions.delimiters = ["[[", "]]"];

app.mount("#app");
