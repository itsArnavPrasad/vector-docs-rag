import { buildIndex } from "../api";

export default function BuildIndex() {
  const handleBuild = async () => {
    console.log("Building FAISS index...");
    const res = await buildIndex();
    console.log("Build index response:", res);
    alert(res.data.status);
  };

  return (
    <button
      className="bg-green-500 text-white px-4 py-2 rounded mt-4"
      onClick={handleBuild}
    >
      Build FAISS Index
    </button>
  );
}
