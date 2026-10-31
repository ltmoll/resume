export default function Skills({ groups }) {
  return (
    <div className="skill-groups">
      {groups.map((group) => (
        <div className="skill-group" key={group.category}>
          <h3>{group.category}</h3>
          <ul className="skill-list">
            {group.items.map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
