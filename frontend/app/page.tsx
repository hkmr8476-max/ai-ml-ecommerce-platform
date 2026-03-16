export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-white p-8">
      <section className="max-w-5xl mx-auto space-y-6">
        <h1 className="text-4xl font-bold">ML-Powered E-Commerce Platform</h1>
        <p className="text-slate-300">
          Personalized recommendations, intelligent search, dynamic pricing, and enterprise-grade commerce operations.
        </p>
        <div className="grid md:grid-cols-3 gap-4">
          {['Recommendations', 'Fraud Detection', 'Demand Forecasting'].map((feature) => (
            <article key={feature} className="rounded-xl border border-slate-700 p-4 bg-slate-900">
              <h2 className="font-semibold">{feature}</h2>
              <p className="text-sm text-slate-400">Production-ready module integrated with backend APIs.</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
