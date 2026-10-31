export default function Experience({ jobs }) {
  return (
    <div className="experience-list">
      {jobs.map((job) => (
        <article className="experience-card" key={job.company}>
          <div className="company-heading">
            <h3>{job.company}</h3>
            <p>{job.location}</p>
          </div>
          {job.roles.map((role) => (
            <div className="role" key={role.title}>
              <div className="role-heading">
                <h4>{role.title}</h4>
                <span>{role.dates}</span>
              </div>
              <ul>
                {role.highlights.map((highlight) => (
                  <li key={highlight}>{highlight}</li>
                ))}
              </ul>
            </div>
          ))}
        </article>
      ))}
    </div>
  );
}
