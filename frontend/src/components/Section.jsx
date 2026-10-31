export default function Section({ title, number, children }) {
  return (
    <section className="resume-section">
      <div className="section-heading">
        <span className="section-number">{number}</span>
        <h2>{title}</h2>
      </div>
      {children}
    </section>
  );
}
