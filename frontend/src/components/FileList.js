export default function FileList({ files }) {
  return (
    <div className="mt-4">
      <h2 className="font-semibold">Uploaded Files:</h2>
      <ul className="list-disc pl-5">
        {files.map((f, i) => (
          <li key={i}>{f}</li>
        ))}
      </ul>
    </div>
  );
}
