import React from 'react';
import { Github, Globe, Linkedin, Mail } from 'lucide-react';
import medalCertificate from '/MEDAL CERTIFICATE.jpg';

const technologies = [
  { name: 'React + TypeScript', description: 'Modern frontend with type safety' },
  { name: 'Tailwind CSS', description: 'Utility-first styling framework' },
  { name: 'Shadcn/UI', description: 'Beautiful, accessible components' },
  { name: 'Recharts', description: 'Responsive data visualization' },
  { name: 'Vite', description: 'Lightning-fast build tooling' },
  { name: 'Lucide Icons', description: 'Beautiful, consistent iconography' },
];

const developer = {
  name: 'Abhishek Khadse',
  role: 'Full Stack Developer',
  bio: 'Passionate about cybersecurity and malware analysis. Building tools that help security researchers and analysts work more effectively.',
  social: {
    github: 'https://github.com/abhishek-khadse',
    linkedin: 'https://www.linkedin.com/in/abhishek-khadse45',
    email: 'abhishekkhadse289@gmail.com',
  },
};

export function About() {
  return (
    <div className="space-y-16 animate-fadeIn">
      {/* Hero Section */}
      <section className="space-y-6">
        <div className="max-w-3xl mx-auto text-center space-y-4">
          <h1 className="text-4xl font-bold">👋 Hi, I'm Abhishek Khadse</h1>
          <p className="text-xl text-muted-foreground">
            Welcome to MRET (Malware Reverse Engineering Toolkit), a comprehensive platform
            built to streamline and enhance malware analysis workflows.
          </p>
        </div>
      </section>

      {/* Tech Stack */}
      <section className="space-y-8">
        <h2 className="text-3xl font-bold">🔧 Tech Stack</h2>
        <div className="grid gap-6 md:grid-cols-2">
          <div className="space-y-4">
            <div className="grid gap-4 grid-cols-2">
              {technologies.map((tech) => (
                <div key={tech.name} className="rounded-lg border bg-card p-4 hover:shadow-md transition-shadow">
                  <h3 className="font-semibold">{tech.name}</h3>
                  <p className="text-sm text-muted-foreground">{tech.description}</p>
                </div>
              ))}
            </div>
          </div>
          <div className="space-y-4">
            <div className="rounded-lg border bg-card p-6">
              <h3 className="text-xl font-semibold mb-4">Core Features</h3>
              <ul className="space-y-3 text-muted-foreground">
                <li>• Static Analysis of PE/ELF files</li>
                <li>• Dynamic Behavior Analysis</li>
                <li>• Network Traffic Analysis</li>
                <li>• ML-based Malware Classification</li>
                <li>• Comprehensive Reporting</li>
                <li>• Real-time Monitoring</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Project Goals */}
      <section className="space-y-8">
        <h2 className="text-3xl font-bold">🚀 Project Goals</h2>
        <div className="grid gap-6 md:grid-cols-2">
          <div className="space-y-4">
            <p className="text-lg text-muted-foreground">
              MRET was created to provide security researchers and analysts with a modern,
              efficient toolkit for malware analysis. The goal is to combine powerful analysis
              capabilities with an intuitive interface.
            </p>
            <div className="rounded-lg border bg-card p-6">
              <h3 className="text-xl font-semibold mb-4">Key Objectives</h3>
              <ul className="space-y-3 text-muted-foreground">
                <li>• Streamline malware analysis workflows</li>
                <li>• Provide comprehensive analysis tools</li>
                <li>• Enable rapid threat assessment</li>
                <li>• Generate detailed, actionable reports</li>
              </ul>
            </div>
          </div>
          <div className="rounded-lg border bg-card overflow-hidden">
            <img
              src="/images/dashboard-preview.jpg"
              alt="Cybersecurity Dashboard"
              className="w-full h-full object-cover"
            />
          </div>
        </div>
      </section>

      {/* Challenges & Learning */}
      <section className="space-y-8">
        <h2 className="text-3xl font-bold">🧩 Challenges & What I Learned</h2>
        <div className="grid gap-6 md:grid-cols-2">
          <div className="rounded-lg border bg-card p-6">
            <h3 className="text-xl font-semibold mb-4">Technical Challenges</h3>
            <ul className="space-y-3 text-muted-foreground">
              <li>• Safe malware execution environment</li>
              <li>• Complex binary analysis algorithms</li>
              <li>• Real-time behavior monitoring</li>
              <li>• ML model training and optimization</li>
            </ul>
          </div>
          <div className="rounded-lg border bg-card p-6">
            <h3 className="text-xl font-semibold mb-4">Key Learnings</h3>
            <ul className="space-y-3 text-muted-foreground">
              <li>• Advanced reverse engineering techniques</li>
              <li>• Machine learning for malware detection</li>
              <li>• Secure sandbox implementation</li>
              <li>• Performance optimization strategies</li>
            </ul>
          </div>
        </div>
      </section>

      {/* What's Next */}
      <section className="space-y-8">
        <h2 className="text-3xl font-bold">👨‍💻 What's Next</h2>
        <div className="rounded-lg border bg-card p-6">
          <p className="text-lg text-muted-foreground mb-4">
            The field of malware analysis is constantly evolving, and so is MRET. Here's what's on the horizon:
          </p>
          <div className="grid gap-4 md:grid-cols-3">
            <div className="p-4 border rounded-lg">
              <h4 className="font-semibold mb-2">Advanced Analysis</h4>
              <p className="text-sm text-muted-foreground">Implementing deeper binary analysis and pattern recognition</p>
            </div>
            <div className="p-4 border rounded-lg">
              <h4 className="font-semibold mb-2">Cloud Integration</h4>
              <p className="text-sm text-muted-foreground">Adding cloud-based analysis capabilities</p>
            </div>
            <div className="p-4 border rounded-lg">
              <h4 className="font-semibold mb-2">Collaboration</h4>
              <p className="text-sm text-muted-foreground">Building features for team-based analysis</p>
            </div>
          </div>
        </div>
      </section>

      {/* Connect */}
      <section className="space-y-6">
        <h2 className="text-3xl font-bold text-center">Let's Connect</h2>
        <div className="max-w-2xl mx-auto text-center">
          <p className="text-lg text-muted-foreground mb-6">
            Interested in malware analysis or want to contribute to MRET? 
            Feel free to reach out through any of these channels:
          </p>
          <div className="flex justify-center space-x-6">
            <a 
              href={developer.social.github} 
              target="_blank" 
              rel="noopener noreferrer" 
              className="text-muted-foreground hover:text-primary transition-colors p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
            >
              <Github className="h-8 w-8" />
              <span className="sr-only">GitHub</span>
            </a>
            <a 
              href={developer.social.linkedin} 
              target="_blank" 
              rel="noopener noreferrer" 
              className="text-muted-foreground hover:text-primary transition-colors p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
            >
              <Linkedin className="h-8 w-8" />
              <span className="sr-only">LinkedIn</span>
            </a>
            <a 
              href={`mailto:${developer.social.email}`} 
              className="text-muted-foreground hover:text-primary transition-colors p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
            >
              <Mail className="h-8 w-8" />
              <span className="sr-only">Email</span>
            </a>
          </div>
        </div>
      </section>

      {/* Medal Certificate */}
      <section className="space-y-8 border-t pt-16">
        <h2 className="text-3xl font-bold text-center flex items-center justify-center gap-2">
          <span>🏆</span> Recognition
        </h2>
        <div className="max-w-4xl mx-auto">
          <div className="rounded-lg border bg-card p-8 space-y-6">
            <div className="aspect-video relative overflow-hidden rounded-lg">
              <img
                src="/images/medal-certificate.jpg"
                alt="Medal Certificate"
                className="w-full h-full object-contain"
              />
            </div>
            <div className="space-y-4 text-center">
              <h3 className="text-2xl font-semibold">Academic Excellence Recognition</h3>
              <p className="text-lg text-muted-foreground">
                Honored to receive recognition for outstanding academic achievement and innovative contribution 
                in the field of malware analysis through the development of MRET. This certificate represents 
                not just personal achievement, but the validation of the project's impact and technical merit 
                in addressing real-world cybersecurity challenges.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t py-8">
        <p className="text-sm text-center text-muted-foreground">
          © 2024 MRET. Built with 💻 by Abhishek Khadse
        </p>
      </footer>
    </div>
  );
}