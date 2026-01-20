export default function ErrorCard({ message }) {
  return (
    <div className="bg-red-50 border border-red-200 rounded-xl p-4 mb-8 text-red-700">
      {message}
    </div>
  );
}
