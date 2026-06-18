import ArtifactOutput from "./components/ArtifactOutput";
import GeneratorForm from "./components/GeneratorForm";
import LoadingSpinner from "./components/LoadingSpinner";
import { useGenerate } from "./hooks/useGenerate";

export default function App() {
  const { data, loading, error, generate } = useGenerate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-white">
      <header className="border-b border-gray-100 bg-white/80 backdrop-blur-sm sticky top-0 z-10">
        <div className="max-w-5xl mx-auto px-6 py-4 flex items-center gap-3">
          <div className="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center shadow-sm">
            <span className="text-white font-bold text-sm">D</span>
          </div>
          <div>
            <span className="font-bold text-gray-900">DiscoveryAI</span>
            <span className="ml-2 text-xs text-gray-400">AI-Powered Artifact Generator</span>
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-12 grid lg:grid-cols-2 gap-12">
        <section>
          <h2 className="text-2xl font-bold text-gray-900 mb-1">Describe Your Product</h2>
          <p className="text-gray-500 text-sm mb-8">
            Paste a plain-English description — get structured SRS, user stories, or code
            scaffolding instantly.
          </p>
          <GeneratorForm onSubmit={generate} loading={loading} />
        </section>

        <section>
          <h2 className="text-2xl font-bold text-gray-900 mb-1">Generated Output</h2>
          <p className="text-gray-500 text-sm mb-8">
            Your structured artifacts appear here, ready to copy.
          </p>

          {loading && <LoadingSpinner />}

          {error && !loading && (
            <div className="p-4 bg-red-50 border border-red-200 rounded-xl text-sm text-red-700">
              <strong>Error:</strong> {error}
            </div>
          )}

          {data && !loading && <ArtifactOutput data={data} />}

          {!data && !loading && !error && (
            <div className="flex flex-col items-center justify-center py-16 text-center border-2 border-dashed border-gray-200 rounded-xl text-gray-400">
              <p className="text-sm">Generated artifacts will appear here.</p>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}
