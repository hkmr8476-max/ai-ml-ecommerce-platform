import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'ML AI Ecommerce',
  description: 'AI-powered ecommerce platform'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
