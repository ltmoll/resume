export default function ProfileHeader({ profile }) {
  return (
    <header className="profile-header">
      <p className="eyebrow">Resume · {profile.location}</p>
      <h1>{profile.name}</h1>
      <p className="profile-title">{profile.title}</p>
      <p className="profile-summary">{profile.summary}</p>
      <a className="contact-link" href={`mailto:${profile.email}`}>
        {profile.email}
        <span aria-hidden="true"> ↗</span>
      </a>
      <a className="contact-link-linkedin" href="https://www.linkedin.com/in/lucas-tremblay-moll-8b744917a/">
        LinkedIn
        <span aria-hidden="true"> ↗</span>
      </a>
    </header>
  );
}
