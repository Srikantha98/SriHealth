export default function ResultCard({ result }) {
  if (!result) {
    return (
      <div className="text-slate-500 text-sm">
        No prediction available. Please upload an MRI image.
      </div>
    );
  }

  const confidenceColor =
    result.confidence >= 85
      ? "text-green-600"
      : result.confidence >= 70
      ? "text-yellow-600"
      : "text-red-600";

  return (
    <div className="space-y-4">
      <div className="p-4 rounded-xl bg-slate-50 border">
        <h4 className="text-lg font-semibold mb-2">
          Prediction Outcome
        </h4>

        <p className="text-slate-700">
          <span className="font-medium">Alzheimer’s Stage:</span>{" "}
          <span className="font-semibold">{result.class}</span>
        </p>

        <p className="text-slate-700">
          <span className="font-medium">Confidence Score:</span>{" "}
          <span className={`font-semibold ${confidenceColor}`}>
            {result.confidence}%
          </span>
        </p>
      </div>

      <div className="text-xs text-slate-500 leading-relaxed">
        <p>
          *The prediction is generated using a GAN-augmented deep learning
          framework and is intended for academic and research purposes only.
        </p>
      </div>
    </div>
  );
}
