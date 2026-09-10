#!/usr/bin/env python3
"""Verify CSS integrity."""
import re

css = open("/home/dawg0/.hermes/Projects/cannalog/.worktrees/t_78d40822/docs/landing-page/styles.css").read()

# Count braces
op = css.count("{")
cl = css.count("}")
print(f"CSS braces: open={op}, close={cl}, balanced={op==cl}")
print(f"CSS total lines: {len(css.splitlines())}")
print(f"CSS total bytes: {len(css):,}")

# Verify key selectors present
selectors = [
    ".hero", ".features", ".gallery", ".roadmap", ".platforms",
    ".email-capture", ".footer", ".btn--primary", ".feature-card",
    ".phone-mockup", ".badge--soon", ".badge--dev", ".badge--planned",
    ".email-form", "@media (max-width: 640px)", "prefers-reduced-motion",
    "--neon-green", "--glow-green", "@keyframes fade-up"
]
print("\nKey selectors/properties:")
for sel in selectors:
    found = sel in css
    print(f"  {sel}: {'OK' if found else 'MISSING'}")
