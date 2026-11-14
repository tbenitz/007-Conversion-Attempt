# GoldenEye 007 Campaign Edition

This branch contains an offline builder for the campaign-only interface. The existing development and progress tracking stay on `main`.

## Build and play

1. Download [Build-Campaign.html](Build-Campaign.html) using GitHub's **Download raw file** button.
2. Open the downloaded builder in Chrome. Choose your local `GoldenEye_v68_TRAIN_EXIT.html`. If you have a ZIP, extract the HTML first.
3. Click **Build & download** and open `GoldenEye_007_Campaign.html` in Chrome.

No installation, server, or upload is needed. This builder only accepts the v6.8 Train Exit HTML. The game assets are provided by your local file and are not in this branch.

The campaign edition retains the 20 missions, briefings, difficulty levels, four dossiers, Q Watch, mission objectives, and the existing Train escape flow. The mission picker shows **Cleared** only for completions saved in that dossier. Explorer, advanced settings, and the corresponding sandbox shortcuts are not exposed in the campaign build. To keep development tools and tracking, continue using the original build and `main`.

Save data stays local to the browser. Chrome may give the new local HTML its own save storage, so an existing dossier may not transfer automatically.
