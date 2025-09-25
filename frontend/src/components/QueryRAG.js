import { useState } from "react";
import { queryRAG } from "../api";

export default function QueryRAG({ onAnswer }) {
  const [query, setQuery] = useState("");

  const handleQuery = async () => {
    if (!query) return;
    console.log("Querying RAG with:", query);
    const res = await queryRAG(query);
    console.log("RAG response:", res);
    onAnswer(res.data.answer);
  };

  return (
    <div className="mt-4 flex gap-2">
      <input
        type="text"
        className="border p-2 flex-1 rounded"
        placeholder="Ask a question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button
        className="bg-purple-500 text-white px-4 py-2 rounded"
        onClick={handleQuery}
      >
        Query
      </button>
    </div>
  );
}
