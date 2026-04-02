import sys

clay_css = """
/* Claymorphism */
/* Primary Clay Button */
.clay-btn-primary {
    background-color: #2563EB;
    border-radius: 9999px;
    box-shadow: 
        8px 8px 16px rgba(0, 0, 0, 0.4), 
        inset -4px -4px 10px rgba(17, 24, 39, 0.5), 
        inset 4px 4px 10px rgba(147, 197, 253, 0.5);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    color: #ffffff;
    border: none;
    display: inline-block;
}
.clay-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 
        12px 12px 20px rgba(0, 0, 0, 0.5), 
        inset -4px -4px 10px rgba(17, 24, 39, 0.5), 
        inset 4px 4px 10px rgba(147, 197, 253, 0.6);
}
.clay-btn-primary:active {
    transform: translateY(2px) scale(0.98);
    box-shadow: 
        2px 2px 5px rgba(0, 0, 0, 0.4), 
        inset -2px -2px 5px rgba(17, 24, 39, 0.5), 
        inset 2px 2px 5px rgba(147, 197, 253, 0.3);
}

/* Secondary Clay Button */
.clay-btn-surface {
    background-color: #25252D;
    border-radius: 9999px;
    box-shadow: 
        8px 8px 16px rgba(0, 0, 0, 0.4), 
        inset -4px -4px 10px rgba(0, 0, 0, 0.5), 
        inset 4px 4px 10px rgba(255, 255, 255, 0.1);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    color: #ffffff;
    border: none;
    display: inline-block;
}
.clay-btn-surface:hover {
    transform: translateY(-2px);
    box-shadow: 
        12px 12px 20px rgba(0, 0, 0, 0.5), 
        inset -4px -4px 10px rgba(0, 0, 0, 0.5), 
        inset 4px 4px 10px rgba(255, 255, 255, 0.15);
}
.clay-btn-surface:active {
    transform: translateY(2px) scale(0.98);
    box-shadow: 
        2px 2px 5px rgba(0, 0, 0, 0.4), 
        inset -2px -2px 5px rgba(0, 0, 0, 0.5), 
        inset 2px 2px 5px rgba(255, 255, 255, 0.05);
}

/* Clay Badge for Roadmap & Steps */
.clay-badge {
    background-color: #2563EB;
    box-shadow: 
        6px 6px 14px rgba(0, 0, 0, 0.4), 
        inset -4px -4px 8px rgba(17, 24, 39, 0.5), 
        inset 4px 4px 8px rgba(147, 197, 253, 0.5);
    border: none;
}
.clay-badge-cyan {
    background-color: #00f4fe;
    box-shadow: 
        6px 6px 14px rgba(0, 0, 0, 0.3), 
        inset -4px -4px 8px rgba(0, 160, 168, 0.4), 
        inset 4px 4px 8px rgba(255, 255, 255, 0.5);
    color: #0E0E13;
    border: none;
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '/* Claymorphism */' not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + clay_css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace button classes
html = html.replace('class="px-6 py-2 bg-primary rounded-full font-bold text-white shadow-glow-secondary scale-hover transition-all"', 'class="px-6 py-2 clay-btn-primary font-bold text-white"')
html = html.replace('class="px-8 py-3 bg-primary rounded-full font-bold text-white shadow-2xl scale-hover transition-all text-lg shadow-glow-secondary"', 'class="px-8 py-3 clay-btn-primary font-bold text-white text-lg"')
html = html.replace('class="px-8 py-3 bg-surface-variant-40 border border-outline-30 rounded-full font-bold text-on-surface-80 hover-text-white scale-hover transition-all hover-border-secondary z-10 text-lg"', 'class="px-8 py-3 clay-btn-surface font-bold text-white z-10 text-lg"')

# Badges
html = html.replace('bg-secondary-10 border border-secondary-30 flex items-center justify-center shadow-step-icon group-hover:shadow-step-icon-hover transition-all', 'clay-badge-cyan flex items-center justify-center transition-all')
html = html.replace('bg-primary-10 border border-primary-30 flex items-center justify-center shadow-step-icon-primary group-hover:shadow-step-icon-primary-hover transition-all', 'clay-badge flex items-center justify-center transition-all')
html = html.replace('bg-secondary-10 border border-secondary-30 flex items-center justify-center', 'clay-badge-cyan flex items-center justify-center')
html = html.replace('bg-primary-10 border border-primary-30 flex items-center justify-center', 'clay-badge flex items-center justify-center')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Claymorphism aplicado com sucesso!')
