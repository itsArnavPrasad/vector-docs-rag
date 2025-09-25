export default function AnswerDisplay({ answer }) {
  if (!answer) return null;
  return (
    <div className="mt-4 p-4 bg-gray-100 rounded shadow">
      <h3 className="font-semibold mb-2">Answer:</h3>
      <p>{answer}</p>
    </div>
  );
}
