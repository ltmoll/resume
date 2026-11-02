import { useEffect, useState } from "react";

import Education from "./components/Education.jsx";
import Experience from "./components/Experience.jsx";
import ProfileHeader from "./components/ProfileHeader.jsx";
import Section from "./components/Section.jsx";
import Skills from "./components/Skills.jsx";

// Vite exposes browser-safe environment variables with the VITE_ prefix.
const PROFILE_URL =
  import.meta.env.VITE_API_URL || "/api/profile";

export default function App() {
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState("");
  const [theme, setTheme] = useState("ocean");
  const [layout, setLayout] = useState("editorial");

  useEffect(() => {
    const controller = new AbortController();

    // Load the content from Flask and cancel the request if this page unmounts.
    async function loadProfile() {
      try {
        const response = await fetch(PROFILE_URL, { signal: controller.signal });
        if (!response.ok) {
          throw new Error(`The resume API returned ${response.status}.`);
        }
        setProfile(await response.json());
      } catch (requestError) {
        if (requestError.name !== "AbortError") {
          setError(requestError.message);
        }
      }
    }

    loadProfile();
    return () => controller.abort();
  }, []);

  if (error) {
    return (
      <main className="page-shell">
        <div className="notice" role="alert">
          <h1>Could not load the resume</h1>
          <p>{error}</p>
          <p>Make sure the Python API is running, then refresh this page.</p>
        </div>
      </main>
    );
  }

  if (!profile) {
    return (
      <main className="page-shell">
        <p className="loading" role="status">Loading resume…</p>
      </main>
    );
  }

  return (
    // These attributes let theme colors and page layout stay independently configurable.
    <main className="page-shell" data-theme={theme} data-layout={layout}>
      <div className="page-content">
        <div className="appearance-controls" aria-label="Appearance options">
          <label>
            Theme
            <select value={theme} onChange={(event) => setTheme(event.target.value)}>
              <option value="ocean">Ocean</option>
              <option value="forest">Forest</option>
              <option value="plum">Plum</option>
            </select>
          </label>
          <label>
            Layout
            <select
              value={layout}
              onChange={(event) => setLayout(event.target.value)}
            >
              <option value="editorial">Editorial</option>
              <option value="stacked">Stacked</option>
            </select>
          </label>
        </div>

        <ProfileHeader profile={profile} />

        <div className="content-grid">
          <div className="main-column">
            <Section title="Experience" number="01">
              <Experience jobs={profile.experience} />
            </Section>
            <Section title="Education" number="02">
              <Education entries={profile.education} />
            </Section>
          </div>

          <aside className="side-column">
            <Section title="Skills" number="03">
              <Skills groups={profile.skills} />
            </Section>
            <Section title="Languages" number="04">
              <ul className="language-list">
                {profile.languages.map((language) => (
                  <li key={language}>{language}</li>
                ))}
              </ul>
            </Section>
          </aside>
        </div>

        <footer className="page-footer">
          <span>{profile.name}</span>
          <a href={`mailto:${profile.email}`}>Get in touch</a>
        </footer>
      </div>
    </main>
  );
}
