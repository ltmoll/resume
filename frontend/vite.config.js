import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    // Keep browser requests on the Vite origin and forward API calls to Flask.
    // This also works when Vite chooses a port other than 5173.
    proxy: {
      "/api": "http://127.0.0.1:5000",
    },
  },
});
