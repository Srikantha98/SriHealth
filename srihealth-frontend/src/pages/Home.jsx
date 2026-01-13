import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white text-slate-800 flex flex-col">
      {/* Navbar */}
      <header className="bg-white shadow-sm">
        <nav className="container mx-auto flex items-center justify-between px-6 py-5">
          <h1 className="text-xl font-semibold tracking-wide">
            SriHealth
          </h1>
          <div className="flex space-x-4">
            <Link
              to="/login"
              className="px-4 py-2 rounded-xl border border-slate-300 hover:bg-slate-100 transition"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="px-4 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 transition"
            >
              Register
            </Link>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <main className="flex-1">
        <section className="container mx-auto px-6 py-20 grid md:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-4xl font-bold leading-tight">
              ACGAN‑Augmented Deep Learning Framework for{" "}
              <span className="text-slate-600">Alzheimer’s Disease Detection</span>
            </h2>
            <p className="mt-6 text-lg text-slate-600">
              An intelligent medical decision‑support system that classifies Alzheimer’s disease stages from MRI images using GAN‑based data augmentation and attention‑driven deep learning.
            </p>
            <div className="mt-8 flex flex-wrap gap-4">
              <Link
                to="/login"
                className="px-6 py-3 rounded-2xl bg-slate-900 text-white text-lg hover:bg-slate-800 transition"
              >
                Get Started
              </Link>
              <a
                href="#overview"
                className="px-6 py-3 rounded-2xl border border-slate-300 text-lg hover:bg-slate-100 transition"
              >
                Learn More
              </a>
            </div>
          </div>

          <div className="flex justify-center">
            <div className="w-80 h-80 rounded-3xl bg-slate-100 shadow-inner flex items-center justify-center text-slate-500">
              MRI Image Analysis
            </div>
          </div>
        </section>

        {/* Overview Section */}
        <section id="overview" className="bg-slate-50 py-16 px-6">
          <h3 className="text-3xl font-semibold text-center mb-10">Project Overview</h3>
          <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            <Card title="Problem Statement">
              Early and accurate diagnosis of Alzheimer’s disease using MRI images is challenging due to limited labeled data and subtle anatomical variations.
            </Card>
            <Card title="Proposed Solution">
              A GAN‑based data augmentation strategy combined with an attention‑based deep neural network to improve classification accuracy and robustness.
            </Card>
            <Card title="Outcome">
              Secure, authenticated web application that predicts Alzheimer’s disease stages and assists clinicians and researchers.
            </Card>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-slate-900 text-slate-200 py-6 text-center">
        <p>Srikantha L / M.Tech CSE • University of Visvesvaraya College of Engineering (UVCE)</p>
      </footer>
    </div>
  );
}

// Reusable Card component
function Card({ title, children }) {
  return (
    <div className="p-6 rounded-2xl bg-white shadow hover:shadow-md transition">
      <h4 className="text-xl font-semibold mb-3">{title}</h4>
      <p className="text-slate-600">{children}</p>
    </div>
  );
}
