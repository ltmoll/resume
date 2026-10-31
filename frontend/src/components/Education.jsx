export default function Education({ entries }) {
  return (
    <div className="education-list">
      {entries.map((entry) => (
        <article className="education-entry" key={entry.school}>
          <div className="education-heading">
            <h3>{entry.school}</h3>
            <span>{entry.dates}</span>
          </div>
          <p>{entry.credential}</p>
        </article>
      ))}
    </div>
  );
}
