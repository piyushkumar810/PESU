export default function HoverButton() {
  return (
    <div className="p-10">
      <button className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-red-500 hover:scale-110 transition">
        Hover Me
      </button>
    </div>
  );
}