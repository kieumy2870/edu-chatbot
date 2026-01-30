import React, { useState } from "react";

export default function MathSolver() {
  const [text, setText] = useState("");
  const [image, setImage] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSolve = async () => {
    setLoading(true);
    const formData = new FormData();
    if (text) formData.append("text", text);
    if (image) formData.append("image", image);

    try {
      const response = await fetch("http://localhost:8000/solve", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResult(data.solution);
    } catch (error) {
      setResult("Lỗi: Không thể kết nối đến server.");
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white shadow-lg rounded-xl">
      <h1 className="text-2xl font-bold mb-4">🤖 AI Math Tutor</h1>
      <textarea
        className="w-full p-3 border rounded mb-4"
        placeholder="Nhập đề bài..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <input
        type="file"
        onChange={(e) => setImage(e.target.files[0])}
        className="mb-4 block"
        accept="image/*"
      />
      <button
        onClick={handleSolve}
        disabled={loading}
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
      >
        {loading ? "Đang giải..." : "Giải bài toán"}
      </button>

      {result && (
        <div className="mt-6 p-4 bg-gray-50 border-l-4 border-blue-500 whitespace-pre-wrap">
          {result}
        </div>
      )}
    </div>
  );
}
