# TASK
Create a rich, infographic-style HTML presentation (a single self-contained HTML slide deck)
based on the INPUT DATA above. You must comply with the DELIVERABLE REQUIREMENTS.
When building each slide, refer to the SLIDE LAYOUT EXAMPLES and choose the most
appropriate layout. Reuse the HTML TEMPLATE provided below.
Do not abbreviate your answer — output all of the code in full.

# LANGUAGE
- All generated output content (slide titles, text, labels, chart legends, table headers,
  navigation buttons, etc.) must be written in Japanese.

# DELIVERABLE REQUIREMENTS
- Produce a single HTML file containing all HTML, CSS, and JavaScript.
- Display only one slide at a time; implement page-switching with JavaScript.
- Support navigation via on-screen buttons AND keyboard arrow keys (Left/Right).
- Display a page indicator showing "current / total" (e.g., 3 / 8).
- Derive the total slide count dynamically
  (e.g., const totalSlides = document.querySelectorAll('.slide').length;),
  so navigation never breaks if the number of slides changes.
- Use Chart.js (`<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>`)
  to visualize data and add interactive dashboards.
  - Initialize every chart (use a per-chart init function or a loop); do not leave any
    canvas uninitialized.
  - Set maintainAspectRatio: false with a fixed container height so charts scale correctly
    on mobile.
- Ensure each slide's layout elements (title, text, figures, etc.) are sized appropriately.
- Use SVG to create and display figures and icons.
  - Add alt/aria-label (or <title>/role="img") to SVGs and ensure sufficient color contrast.
- Emphasize a modern, professional corporate design throughout, using purple (#A100FF)
  as the accent color.
- Use the 'Noto Sans JP' font with 'sans-serif' as the fallback.
- Adopt a responsive design that adapts to various screen sizes.
- Allow long-content slides to scroll (overflow: auto) so text is never clipped.
- Place appropriate charts/graphs on each slide to visualize data.
- Generate between 6 and 10 slides depending on the volume of input data.

# DATA INTEGRITY
- When source figures or tables exist, read the values precisely (to the decimal point)
  and reproduce them accurately.
- Do NOT invent or fabricate data. If a value is missing in the INPUT DATA,
  mark it as "N/A" instead of guessing.

# CHART STYLE
- For bar charts, pie charts, etc., create a colorful, well-organized dashboard while
  keeping #A100FF as the primary accent and maintaining a clean, professional look.

# SLIDE LAYOUT EXAMPLES
1. Overview / Summary slide
   - Main title
   - 3–5 key points (bullet list)
   - Short supporting description
2. Data Analysis slide
   - Section title
   - Graph or chart showing key data
   - Short text with interpretation / insight
3. Process / Flow slide
   - Process name or overview
   - Flowchart or diagram showing steps
   - Brief description of each step
4. Comparison slide
   - Comparison title
   - 2–4 item comparison table or contrast diagram
   - Summary of key differences or conclusions
5. Timeline / Plan slide
   - Project or plan name
   - Time-based visualization (e.g., Gantt chart)
   - Key milestones or phases

Common requirements for every slide:
- Clear structure and hierarchy
- Balance between visual elements and text
- One primary message per slide
- Concise, easy-to-understand wording
- Appropriate whitespace and layout
- Slide navigation controls (Previous / Next)

# HTML TEMPLATE
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>プレゼンテーションタイトル</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');

        body, html {
            margin: 0;
            padding: 0;
            font-family: 'Noto Sans JP', sans-serif;
            background-color: #f0f0f0;
            color: #333;
        }
        .slide {
            width: 100vw;
            height: 100vh;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
            box-sizing: border-box;
            overflow: auto;
        }
        .slide.active { display: flex; }
        h1 { font-size: 2.5rem; color: #A100FF; margin-bottom: 1rem; }
        h2 { font-size: 2rem; color: #333; margin-bottom: 1rem; }
        p { font-size: 1.2rem; line-height: 1.6; margin-bottom: 1rem; }
        ul { text-align: left; font-size: 1.2rem; line-height: 1.6; }
        .chart-container {
            position: relative;
            width: 80%;
            max-width: 600px;
            height: 400px;
            margin: 1rem auto;
        }
        .nav-buttons {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .page-indicator {
            position: fixed;
            bottom: 2.4rem;
            left: 2rem;
            font-size: 1rem;
            color: #A100FF;
            font-weight: 700;
        }
        button {
            background-color: #A100FF; color: white; border: none;
            padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer;
            border-radius: 5px; transition: background-color 0.3s;
        }
        button:hover { background-color: #8400cc; }
        .table-container { width: 90%; max-width: 1000px; margin: 1rem auto; overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; white-space: nowrap; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #A100FF; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        .comparison-container { display: flex; justify-content: space-around; align-items: stretch; width: 100%; margin-top: 20px; }
        .comparison-item {
            background-color: #fff; border-radius: 10px; padding: 20px; margin: 0 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1); flex: 1;
            display: flex; flex-direction: column; justify-content: space-between;
        }
        .comparison-item h3 { color: #A100FF; margin-bottom: 10px; font-size: 1.2rem; }
        .comparison-item p { margin-bottom: 5px; font-size: 1rem; }
        .highlight { font-weight: bold; color: #A100FF; }
        .examples-container {
            background-color: #fff; border-radius: 10px; padding: 15px;
            margin-top: 20px; text-align: left; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .examples-container h3 { color: #A100FF; margin-bottom: 10px; }
        .examples-container ul { list-style-type: none; padding-left: 0; }
        .examples-container li { margin-bottom: 5px; }
        @media (max-width: 768px) {
            .comparison-container { flex-direction: column; }
            .comparison-item { margin: 10px 0; }
            .chart-container { height: 300px; }
            table { font-size: 0.9rem; }
            th, td { padding: 8px; }
        }
    </style>
</head>
<body>
    <div id="slide1" class="slide active">
        <h1>メインタイトル</h1>
        <p>サブタイトルまたは説明</p>
    </div>
    <div id="slide2" class="slide">
        <h2>スライドタイトル</h2>
        <ul><li>項目1</li><li>項目2</li><li>項目3</li></ul>
    </div>
    <div id="slide3" class="slide">
        <h2>グラフタイトル</h2>
        <div class="chart-container"><canvas id="chartCanvas"></canvas></div>
    </div>
    <div id="slide4" class="slide">
        <h2>表タイトル</h2>
        <div class="table-container">
            <table>
                <tr><th>列1</th><th>列2</th><th>列3</th></tr>
                <tr><td>データ1</td><td>データ2</td><td>データ3</td></tr>
            </table>
        </div>
    </div>
    <div id="slide5" class="slide">
        <h2>比較タイトル</h2>
        <div class="comparison-container">
            <div class="comparison-item"><h3>項目1</h3><p>説明文</p><p>数値: <span class="highlight">100</span></p></div>
            <div class="comparison-item"><h3>項目2</h3><p>説明文</p><p>数値: <span class="highlight">200</span></p></div>
        </div>
    </div>
    <div id="slide6" class="slide">
        <h2>例示タイトル</h2>
        <div class="examples-container">
            <h3>例の見出し</h3>
            <ul><li>• 例1</li><li>• 例2</li><li>• 例3</li></ul>
        </div>
    </div>

    <div class="page-indicator" id="pageIndicator">1 / 1</div>
    <div class="nav-buttons">
        <button onclick="changeSlide(-1)">前へ</button>
        <button onclick="changeSlide(1)">次へ</button>
    </div>

    <script>
        let currentSlide = 1;
        const totalSlides = document.querySelectorAll('.slide').length;

        function updateIndicator() {
            document.getElementById('pageIndicator').textContent = currentSlide + ' / ' + totalSlides;
        }
        function changeSlide(direction) {
            document.getElementById('slide' + currentSlide).classList.remove('active');
            currentSlide += direction;
            if (currentSlide > totalSlides) currentSlide = 1;
            if (currentSlide < 1) currentSlide = totalSlides;
            document.getElementById('slide' + currentSlide).classList.add('active');
            updateIndicator();
        }
        document.addEventListener('keydown', function (e) {
            if (e.key === 'ArrowRight') changeSlide(1);
            if (e.key === 'ArrowLeft') changeSlide(-1);
        });

        function initCharts() {
            const ctx = document.getElementById('chartCanvas');
            if (ctx) {
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['ラベル1', 'ラベル2', 'ラベル3', 'ラベル4'],
                        datasets: [
                            { label: 'データセット1', data: [12, 19, 3, 5], backgroundColor: '#A100FF' },
                            { label: 'データセット2', data: [2, 3, 20, 5], backgroundColor: '#FF00A1' }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: { y: { beginAtZero: true } }
                    }
                });
            }
        }
        window.addEventListener('load', function () {
            updateIndicator();
            initCharts();
        });
    </script>
</body>
</html>
```
