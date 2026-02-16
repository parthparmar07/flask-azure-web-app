# Flask Azure Demo

A simple Flask application deployed to Azure App Service using GitHub Actions.

## Local Development

1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Visit http://127.0.0.1:5000

## Deployment

This app is configured for automatic deployment to Azure App Service via GitHub Actions.

- Push to the `main` branch to trigger deployment.
- Update the `app-name` in `.github/workflows/deploy.yml` with your Azure Web App name.
- Ensure the `AZURE_WEBAPP_PUBLISH_PROFILE` secret is set in GitHub repository settings.

## API Endpoints

- `/` - Home page
- `/health` - Health check
- `/api/data` - Sample API endpoint